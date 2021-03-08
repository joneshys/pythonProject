resource "aws_db_instance" "db_instance" {
  multi_az = false
  publicly_accessible = false
  instance_class = "db.t2.small"
  allocated_storage    = 20
  port = 58963
  storage_type = "gp2"
  engine = "mysql"
  identifier= var.db-instance-name
  name = var.db-instance-name
  username = "joneshys"
  password = "Neruda87"
  parameter_group_name = "default.mysql8.0"
  db_subnet_group_name = aws_db_subnet_group.subnet-rds-private-instances.name
  vpc_security_group_ids = [aws_security_group.SG_RDS.id]
  final_snapshot_identifier = "${var.db-instance-name}-${local.timestamp_sanitized}"
  skip_final_snapshot = true
  iam_database_authentication_enabled = true
  tags = {
    environment = "testing"
  }
}

#  backup_retention_period = 7