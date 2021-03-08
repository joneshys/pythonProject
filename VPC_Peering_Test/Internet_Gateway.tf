resource "aws_internet_gateway" "Internet_Gateway_Public_Subnet" {
  vpc_id = aws_vpc.VPC_Test.id
  tags = {
    Name = "Internet_Gateway_Public_Subnet"
  }
}