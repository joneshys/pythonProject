resource "aws_security_group" "SSH_Anyware" {
  name = "${var.project_name}_SSH_Anyware"
  description = "SSH_Anyware inbound to SSH"
  vpc_id = "${aws_default_vpc.VPC_Test.id}"
  ingress {
    from_port = 22
    protocol = "tcp"
    to_port = 22
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port = 0
    protocol = "-1"
    to_port = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "HTTP_Anyware" {
  name = "${var.project_name}_HTTP_Anyware"
  description = "HTTP for Anyware "
  vpc_id = "${aws_default_vpc.VPC_Test.id}"
  ingress {
    from_port = 80
    protocol = "tcp"
    to_port = 80
    cidr_blocks = ["0.0.0.0/0"]
  }
  egress {
    from_port = 0
    protocol = "-1"
    to_port = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}