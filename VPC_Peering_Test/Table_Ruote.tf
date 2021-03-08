resource "aws_route_table" "Route_Table" {
  vpc_id = aws_vpc.VPC_Test.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.Internet_Gateway_Public_Subnet.id
  }
  tags = {
    Name = "Route_Table"
  }
}

resource "aws_route_table_association" "Roue_Table_VPCPublicSubnetACidrBlock" {
  subnet_id = aws_subnet.VPCPublicSubnetACidrBlock.id
  route_table_id = aws_route_table.Route_Table.id
}

resource "aws_route_table_association" "Roue_Table_VPCPublicSubnetBCidrBlock" {
  subnet_id = aws_subnet.VPCPublicSubnetBCidrBlock.id
  route_table_id = aws_route_table.Route_Table.id
}

resource "aws_route_table_association" "Roue_Table_VPCPrivateSubnetACidrBlock" {
  depends_on = [
  aws_subnet.VPCPrivateSubnetACidrBlock, aws_route_table.Route_Table
  ]
  subnet_id = aws_subnet.VPCPrivateSubnetACidrBlock.id
  route_table_id = aws_route_table.Route_Table.id
}

resource "aws_route_table_association" "Roue_Table_VPCPrivateSubnetBCidrBlock" {
  depends_on = [
  aws_subnet.VPCPrivateSubnetBCidrBlock, aws_route_table.Route_Table
  ]
  subnet_id = aws_subnet.VPCPrivateSubnetBCidrBlock.id
  route_table_id = aws_route_table.Route_Table.id
}
