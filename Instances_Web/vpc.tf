resource "aws_default_vpc" "VPC_Test" {
  tags = {
    Name = "${var.project_name}_VPC_Test"
  }
}