resource "aws_eip" "Elastic_IP_Instances" {
  instance = "${aws_instance.web.id}"
  tags = {
    Name = "${var.project_name}_test_EIP"
  }
}