#Creacion de las subnet necesarias en la infraestructura


resource "aws_subnet" "VPCPrivateSubnetACidrBlock" {
  depends_on = [aws_vpc.VPC_Test]
  availability_zone ="us-west-2a"
  cidr_block = "10.170.32.0/26"
  map_public_ip_on_launch = false
  vpc_id = aws_vpc.VPC_Test.id
   tags = {
     Name = "VPCPrivateSubnetACidrBlock"
   }
}

resource "aws_subnet" "VPCPrivateSubnetBCidrBlock" {
  depends_on = [aws_vpc.VPC_Test]
  availability_zone = "us-west-2b"
  cidr_block = "10.170.32.64/26"
  map_public_ip_on_launch = false
  vpc_id = aws_vpc.VPC_Test.id
   tags = {
     Name = "VPCPrivateSubnetBCidrBlock"
   }
}

resource "aws_subnet" "VPCPublicSubnetACidrBlock" {
  depends_on = [aws_vpc.VPC_Test]
  vpc_id = aws_vpc.VPC_Test.id
  cidr_block = "10.170.32.128/27"
  availability_zone = "us-west-2b"
  map_public_ip_on_launch = true
  tags = {Name = "VPCPublicSubnetACidrBlock" }
}

resource "aws_subnet" "VPCPublicSubnetBCidrBlock" {
  depends_on = [aws_vpc.VPC_Test]
  cidr_block = "10.170.32.160/27"
  vpc_id = aws_vpc.VPC_Test.id
  availability_zone = "us-west-2a"
  map_public_ip_on_launch = true
  tags = {Name = "VPCPublicSubnetBCidrBlock"}
}

resource "aws_db_subnet_group" "subnet-rds-private-instances" {
  subnet_ids = [aws_subnet.VPCPrivateSubnetACidrBlock.id,aws_subnet.VPCPrivateSubnetBCidrBlock.id]
}

#Creacion Subnet para DB

#resource "aws_subnet" "VPCPrivateSubnetDBACidrBlock" {
#  depends_on = [aws_vpc.VPC_Test]
#  cidr_block = "10.170.32.192/28"
#  availability_zone = "us-west-2c"
#  map_public_ip_on_launch = false
#  vpc_id = aws_vpc.VPC_Test.id
#   tags = {
#     Name = "VPCPrivateSubnetDBACidrBlock"
#   }
#}

#resource "aws_subnet" "VPCPrivateSubnetDBBCidrBlock" {
#  depends_on = [aws_vpc.VPC_Test]
#  cidr_block = "10.170.32.208/28"
#  availability_zone = "us-west-2c"
#  map_public_ip_on_launch = false
#  vpc_id = aws_vpc.VPC_Test.id
#   tags = {
#     Name = "VPCPrivateSubnetDBBCidrBlock"
#   }
#}



