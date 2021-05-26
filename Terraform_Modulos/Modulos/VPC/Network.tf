resource "aws_vpc" "main-module" {
  cidr_block = var.vpc_cidr
  instance_tenancy = var.tenancy
  tags = {
    Name = "VPC_For_Deploy"
  }
}

resource "aws_subnet" "main-subnet-1" {
  vpc_id = aws_vpc.main-module.id
  cidr_block = var.subnet_cidr
  tags = {
    Name = "Subnet_For_Deploy"
  }
}