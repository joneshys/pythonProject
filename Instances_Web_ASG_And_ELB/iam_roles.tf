resource "aws_iam_role" "Role_RDS_DB_Connect" {
  name = "Role_RDS_DB_Connect"
  assume_role_policy = <<EOF
{
      "Version": "2012-10-17",
      "Statement": [
        {
          "Action": "sts:AssumeRole",
          "Principal": {
            "Service": "rds.amazonaws.com"
          },
          "Effect": "Allow",
          "Sid": ""
        }
      ]
    }
EOF
}

resource "aws_iam_policy" "Policy_RDS_DB_Connect" {
  name = "Policy_RDS_DB_Connect"
  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "rds-db:connect"
            ],
            "Resource": [
                "${aws_db_instance.db_instance.arn}/jbenitez"
            ]
        }
    ]
}
EOF
}

resource "aws_iam_role_policy_attachment" "Attach_RDS_DB_Connect" {
  policy_arn = aws_iam_policy.Policy_RDS_DB_Connect.arn
  role = aws_iam_role.Role_RDS_DB_Connect.name
}
