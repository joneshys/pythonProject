provider "aws" {
  shared_credentials_file = "C:\\Users\\jose.benitez\\.aws"
  profile = "Test_Packer"
  region = "us-east-1"
}

# Providing a reference to our default VPC
resource "aws_vpc" "VPC_Test" {
  cidr_block = "10.170.32.0/24"
  enable_dns_hostnames = true
  tags = {
    Name = "Docker_VPC_Test"
  }
}

resource "aws_subnet" "VPCPrivateSubnetACidrBlock" {
  depends_on = [aws_vpc.VPC_Test]
  availability_zone = "us-east-1a"
  cidr_block = "10.170.32.0/26"
  map_public_ip_on_launch = false
  vpc_id = aws_vpc.VPC_Test.id
   tags = {
     Name = "VPCPrivateSubnetACidrBlock"
   }
}

resource "aws_subnet" "VPCPrivateSubnetBCidrBlock" {
  depends_on = [aws_vpc.VPC_Test]
  availability_zone = "us-east-1b"
  cidr_block = "10.170.32.64/26"
  map_public_ip_on_launch = false
  vpc_id = aws_vpc.VPC_Test.id
   tags = {
     Name = "VPCPrivateSubnetBCidrBlock"
   }
}

resource "aws_subnet" "VPCPublicSubnetACidrBlock" {
  depends_on = [aws_vpc.VPC_Test]
  vpc_id = aws_vpc.VPC_Test.id
  cidr_block = "10.170.32.128/27"
  availability_zone = "us-east-1b"
  map_public_ip_on_launch = true
  tags = {Name = "VPCPublicSubnetACidrBlock" }
}

resource "aws_subnet" "VPCPublicSubnetBCidrBlock" {
  depends_on = [aws_vpc.VPC_Test]
  cidr_block = "10.170.32.160/27"
  vpc_id = aws_vpc.VPC_Test.id
  availability_zone = "us-east-1a"
  map_public_ip_on_launch = true
  tags = {Name = "VPCPublicSubnetBCidrBlock"}
}

resource "aws_db_subnet_group" "subnet-rds-private-instances" {
  subnet_ids = [aws_subnet.VPCPrivateSubnetACidrBlock.id,aws_subnet.VPCPrivateSubnetBCidrBlock.id]
}

resource "aws_ecr_repository" "my_first_ecr_repo" {
  name = "my-first-ecr-repo"
}

resource "aws_ecs_cluster" "my_cluster" {
  name = "my-cluster" # Naming the cluster
}


resource "aws_ecs_task_definition" "my_first_task" {
  family                   = "my-first-task" # Naming our first task
  container_definitions    = <<DEFINITION
  [
    {
      "name": "my-first-task",
      "image": "${aws_ecr_repository.my_first_ecr_repo.repository_url}",
      "essential": true,
      "portMappings": [
        {
          "containerPort": 3000,
          "hostPort": 3000
        }
      ],
      "memory": 512,
      "cpu": 256
    }
  ]
  DEFINITION
  requires_compatibilities = ["FARGATE"] # Stating that we are using ECS Fargate
  network_mode             = "awsvpc"    # Using awsvpc as our network mode as this is required for Fargate
  memory                   = 512         # Specifying the memory our container requires
  cpu                      = 256         # Specifying the CPU our container requires
  execution_role_arn       = aws_iam_role.ecsTaskExecutionRole.arn
}

resource "aws_iam_role" "ecsTaskExecutionRole" {
  name               = "ecsTaskExecutionRole"
  assume_role_policy = data.aws_iam_policy_document.assume_role_policy.json
}

data "aws_iam_policy_document" "assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]

    principals {
      type        = "Service"
      identifiers = ["ecs-tasks.amazonaws.com"]
    }
  }
}

resource "aws_iam_role_policy_attachment" "ecsTaskExecutionRole_policy" {
  role       = aws_iam_role.ecsTaskExecutionRole.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AmazonECSTaskExecutionRolePolicy"
}

resource "aws_alb" "application_load_balancer" {
  name               = "test-lb-tf" # Naming our load balancer
  load_balancer_type = "application"
  subnets = [aws_subnet.VPCPrivateSubnetACidrBlock.id, aws_subnet.VPCPrivateSubnetBCidrBlock.id]
  # Referencing the security group
  security_groups = [aws_security_group.load_balancer_security_group.id]
}

# Creating a security group for the load balancer:
resource "aws_security_group" "load_balancer_security_group" {
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"] # Allowing traffic in from all sources
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_lb_target_group" "target_group" {
  name        = "target-group"
  port        = 80
  protocol    = "HTTP"
  target_type = "ip"
  vpc_id      = aws_vpc.VPC_Test.id # Referencing the default VPC
}

resource "aws_lb_listener" "listener" {
  load_balancer_arn = aws_alb.application_load_balancer.arn # Referencing our load balancer
  port              = "80"
  protocol          = "HTTP"
  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.target_group.arn # Referencing our tagrte group
  }
}

resource "aws_ecs_service" "my_first_service" {
  name            = "my-first-service"                             # Naming our first service
  cluster         = aws_ecs_cluster.my_cluster.id             # Referencing our created Cluster
  task_definition = aws_ecs_task_definition.my_first_task.arn # Referencing the task our service will spin up
  launch_type     = "FARGATE"
  desired_count   = 3 # Setting the number of containers to 3

  load_balancer {
    target_group_arn = aws_lb_target_group.target_group.arn # Referencing our target group
    container_name   = aws_ecs_task_definition.my_first_task.family
    container_port   = 80 # Specifying the container port
  }

  network_configuration {
    subnets          = [aws_subnet.VPCPrivateSubnetBCidrBlock.id, aws_subnet.VPCPrivateSubnetACidrBlock.id]
    assign_public_ip = true                                                # Providing our containers with public IPs
    security_groups  = [aws_security_group.service_security_group.id] # Setting the security group
  }
}


resource "aws_security_group" "service_security_group" {
  ingress {
    from_port = 0
    to_port   = 0
    protocol  = "-1"
    # Only allowing traffic in from the load balancer security group
    security_groups = [aws_security_group.load_balancer_security_group.id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}