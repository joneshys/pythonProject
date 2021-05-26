
output "vpc_id" {
  value = aws_vpc.main-module.id
}

output "subnet_id" {
  value = aws_subnet.main-subnet-1.id
}