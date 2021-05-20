output "sg_id" {
  value = aws_security_group.sg_test.id
}

output "eip" {
  value = aws_eip.eip.public_ip
}

output "kye_pair" {
  value = aws_key_pair.key_pair.key_name
}