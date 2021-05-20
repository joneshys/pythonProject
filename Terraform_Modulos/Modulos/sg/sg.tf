resource "aws_security_group" "sg_test" {
  name = "SG-${var.project_name}-${var.environment}"
  description = "SG-${var.project_name}-${var.environment}"
  vpc_id = "${var.vpc_id}"
  tags = {
    Name = "SG-${var.project_name}-${var.environment}"
  }

  ingress {
    from_port = 22
    protocol = "ALL"
    to_port = 22
    cidr_blocks = ["0.0.0.0/0"]
    description = "SG-${var.project_name}-${var.environment}"
  }

  egress {
    from_port = 0
    protocol = "ALL"
    to_port = 0
    cidr_blocks = ["0.0.0.0/0"]
    description = "SG-${var.project_name}-${var.environment}"
  }
}