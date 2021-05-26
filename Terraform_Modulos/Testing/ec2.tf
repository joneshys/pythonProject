#module "ec2" {
#  source = "../Modulos/sg"
#  sg_name = "ec2-testing"
#  vpc_id = "vpc-0d894a1bc707303a1"
#  project_name = "web"
 #   environment = "testing"
#    instance_type = "t2.micro"
#    ami = "ami-077e31c4939f6a2f3"
#    subnet_id = "subnet-01403b9140f4d9bbe"
#    key_name =
#  }

module "vpc" {
  source = "../Modulos/VPC"
  vpc_cidr = "192.168.0.0/16"
  tenancy = "default"
  vpc_id = module.vpc.vpc_id
  subnet_cidr = "192.168.0.0/24"
}
module "ec2" {
  source = "../Modulos/ec2"
  ec2_count = "1"
  ami_id = "ami-0cf6f5c8a62fa5da6"
  subnet_id = module.vpc.subnet_id
  instance_type = "t2.micro"
}