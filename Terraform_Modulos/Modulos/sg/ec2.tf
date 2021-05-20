resource "aws_instance" "web" {
  ami = var.ami
  key_name = var.key_name
  instance_type = var.instance_type
  tags = {
    Name = "${var.project_name}-${var.environment}"
  }
  vpc_security_group_ids = [
    aws_security_group.sg_test.id
  ]
  subnet_id = var.subnet_id
}