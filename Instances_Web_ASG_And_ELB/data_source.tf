data "aws_ami" "web" {
  most_recent = true

  filter {
    name = "name"
    values = ["amzn2-ami-hvm-2.0.20200917.0-x86_64-gp2*"]
  }

  filter {
    name = "virtualization-type"
    values = ["hvm"]
  }
  owners = ["amazon"]
}

data "template_file" "task_definition_template"{
  template = file("task_definition.json")
  vars = {
    REPOSITORY_URL = replace(aws_ecr_repository.dockerTest.name, "https://", "")
  }
}

