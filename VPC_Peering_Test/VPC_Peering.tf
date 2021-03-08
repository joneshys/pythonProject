resource "aws_vpc_peering_connection" "vpc_peering_connection" {
  peer_vpc_id = ""
  vpc_id = aws_vpc.VPC_Test.id
}