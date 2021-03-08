resource "aws_instance" "web" {
  ami = "${var.ami_id}"
  instance_type = "${var.instances_type}"
  vpc_security_group_ids = [
    "${ aws_security_group.SSH_Anyware.id }", "${aws_security_group.HTTP_Anyware.id}"]
  key_name = "${ aws_key_pair.Test_And_Test.key_name }"
  user_data = "${file("user_data.txt")}"
  tags = {
    Name = "${var.project_name}_Instances_Test"
  }
}