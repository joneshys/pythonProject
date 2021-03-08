resource "aws_launch_configuration" "Instances_Pool_Web" {
  name = "${var.project_name}_LC_Web_"
  image_id = var.ami_id
  instance_type = var.instances_type
  key_name = "Test_Joneshys_Terraform_Key_Pair_Test"
  security_groups = [aws_security_group.HTTP_Anyware.id, aws_security_group.SSH_Anyware.id]
  user_data = file("user_data.txt")
  associate_public_ip_address = true
}
#key_name = aws_key_pair.Test_And_Test.key_name #Se crea con ls key pub de la maquiina(server)