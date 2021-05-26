resource "aws_instance" "web" {
  ami = var.ami_id
  instance_type = var.instance_type
  count = var.ec2_count
  subnet_id = var.subnet_id
  tags = {
    Name ="Maquina-1"
  }
}