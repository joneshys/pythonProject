#Creacion del Balanceador de carga y dos target group
resource "aws_lb" "Elastic_Load_balances_Test" {
  name = "elastic-load-balances-test"
  internal = false
  load_balancer_type = "application"
  security_groups = [aws_security_group.Elastic_Load_balances_Test.id]
  subnets = [aws_subnet.VPCPublicSubnetACidrBlock.id,aws_subnet.VPCPublicSubnetBCidrBlock.id]
  enable_deletion_protection = false
}

# Salida de puerto 80 apache
resource "aws_lb_listener" "Listener_Elastic_Load_balances_Test" {
  load_balancer_arn = aws_lb.Elastic_Load_balances_Test.arn
  port = "80"
  protocol = "HTTP"
  default_action {
    type = "redirect"
    redirect {
      port = "443"
      protocol = "HTTPS"
      status_code = "HTTP_301"
    }
  }
}
resource "aws_lb_target_group" "lb_target_group" {
  name = "lb-target-group"
  port = 80
  protocol = "HTTP"
  vpc_id = aws_vpc.VPC_Test.id
}
resource "aws_lb_listener_rule" "lb-listener-rule" {
  listener_arn = aws_lb_listener.Listener_Elastic_Load_balances_Test.arn
  priority = 1
  action {
    type = "forward"
    target_group_arn = aws_lb_target_group.lb_target_group.arn
  }
  condition {
    path_pattern {
      values = ["/*"]
    }
  }
}

# Salida puerto 3000 DOCKER
resource "aws_lb_listener" "Listener_Elastic_Load_balances_Test_Docker" {
  load_balancer_arn = aws_lb.Elastic_Load_balances_Test.arn
  port = "3000"
  protocol = "HTTP"
  default_action {
    type = "redirect"
    redirect {
      port = "443"
      protocol = "HTTPS"
      status_code = "HTTP_301"
    }
  }
}
resource "aws_lb_target_group" "lb_target_group_docker" {
  name = "lb-target-group-docker"
  port = 3000
  protocol = "HTTP"
  vpc_id = aws_vpc.VPC_Test.id
}
resource "aws_lb_listener_rule" "lb-listener-rule-Docker" {
  listener_arn = aws_lb_listener.Listener_Elastic_Load_balances_Test_Docker.arn
  priority = 2
  action {
    type = "forward"
    target_group_arn = aws_lb_target_group.lb_target_group_docker.arn
  }
  condition {
    path_pattern {
      values = ["/query"]
    }
  }
}
