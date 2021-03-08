resource "aws_vpc" "VPC_Test" {
  cidr_block = "10.170.32.0/24"
  enable_dns_hostnames = true
  tags = {
    Name = "VPC_Test"
  }
}