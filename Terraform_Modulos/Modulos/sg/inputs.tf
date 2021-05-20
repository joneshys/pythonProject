variable "sg_name" {}
variable "vpc_id" {}
variable "project_name" {}
variable "environment" {}
variable "ami" {}
variable "instance_type" {}
variable "key_name" {}
variable "subnet_id" {}
variable "vpc_cidr" {
  default = "10.0.0.0/16"
}