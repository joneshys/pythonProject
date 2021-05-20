output "Instances_Public_IP" {
  value = aws_instance.web.public_ip
}

output "Security_Group_Id" {
  value = aws_security_group.SSH_Anyware.id
}

output "Public_Elastic_IP" {
  value = aws_eip.Elastic_IP_Instances.public_ip
}