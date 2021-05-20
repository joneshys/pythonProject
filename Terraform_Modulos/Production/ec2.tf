module "ec2" {
  source = "../Modulos/sg"
  sg_name = "ec2-Prod"
  vpc_id = "vpc-0d894a1bc707303a1"
  project_name = "web"
  environment = "producctive"
  instance_type = "t2.micro"
  ami = "ami-077e31c4939f6a2f3"
  subnet_id = "subnet-01403b9140f4d9bbe"
  key_name = "KP_Instances"
}