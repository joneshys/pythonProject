#Creacion de grupos de seguridad

resource "aws_security_group" "SSH_Anyware" {
  name = "${var.project_name}_SSH_Anyware"
  description = "SSH_Anyware inbound to SSH"
  vpc_id = aws_vpc.VPC_Test.id
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
  vpc_id = aws_vpc.VPC_Test.id
  ingress {
    from_port = 80
    protocol = "tcp"
    to_port = 80
    security_groups = [aws_security_group.Elastic_Load_balances_Test.id]
  }
  ingress {
    from_port = 3000
    protocol = "tcp"
    to_port = 3000
    cidr_blocks = ["0.0.0.0/0"]
    security_groups = [aws_security_group.Elastic_Load_balances_Test.id]
  }
  egress {
    from_port = 0
    protocol = "-1"
    to_port = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "Elastic_Load_balances_Test" {
  name = "${var.project_name}_Elastic_Load_balances_Test_"
  description = "Balanceador de carga V2"
  vpc_id = aws_vpc.VPC_Test.id
  ingress {
    from_port = 80
    protocol = "tcp"
    to_port = 80
    cidr_blocks = ["0.0.0.0/0"]
    description = "Port 80 para el consumo de apache"
  }
  ingress {
    from_port = 3000
    protocol = "tcp"
    to_port = 3000
    cidr_blocks = ["0.0.0.0/0"]
    description = "Port 3000 para el consumo de la aplicacion de Flask"
  }
  ingress {
    from_port = 433
    protocol = "tcp"
    to_port = 433
    cidr_blocks = ["0.0.0.0/0"]
    description = "Port 443, port HTTPS"
  }
  egress {
    from_port = 0
    protocol = "-1"
    to_port = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "SG_RDS" {
  name = "${var.project_name}_SG_RDS_"
  description = "Grupo de seguridad para el acceso a la DB desde las subnet Privadas"
  vpc_id = aws_vpc.VPC_Test.id
  ingress {
    from_port = 58963
    protocol = "tcp"
    to_port = 58963
    cidr_blocks = ["201.233.219.25/32"]
    security_groups = [aws_security_group.SSH_Anyware.id]
    description = "Ingreso a la DB desde la subnet privada"
  }
  egress {
    from_port = 0
    protocol = "-1"
    to_port = 0
    cidr_blocks = ["0.0.0.0/0"]
  }
}