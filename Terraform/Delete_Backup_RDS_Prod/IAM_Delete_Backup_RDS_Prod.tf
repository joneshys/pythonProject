# Lambda = Creación de lambada para DeleteBackup_RDS_Prod
resource "aws_iam_role" "Role_Access_Lambda" {
  name = "Role_Access_Lambda"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}
resource "aws_iam_policy" "Police_Access_Lambda" {
  name = "Police_Access_Lambda"
  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "logs:CreateLogGroup",
            "Resource": "arn:aws:logs:us-east-1:949375136131:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": [
                "arn:aws:logs:us-east-1:949375136131:log-group:/aws/lambda/DeleteBackup_RDS_Prod:*"
            ]
        }
    ]
}
EOF
}
resource "aws_iam_role_policy_attachment" "Attachment_Access_lambda" {
  policy_arn = aws_iam_policy.Police_Access_Lambda.arn
  role = aws_iam_role.Role_Access_Lambda.name
}
resource "aws_iam_policy" "DeleteBackup_RDS_Prod" {
  name = "Policy_DeleteBackup_RDS_Prod"
  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "rds:DeleteDBSnapshot",
                "rds:DescribeDBInstances",
                "states:StartExecution",
                "rds:DescribeDBSnapshots"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}
resource "aws_iam_role_policy_attachment" "Attachment_DeleteBackup_RDS_Prod" {
  policy_arn = aws_iam_policy.DeleteBackup_RDS_Prod.arn
  role = aws_iam_role.Role_Access_Lambda.name
}

resource "aws_cloudwatch_event_rule" "Rule_Delete_Backup_RDS_Prod" {
  name = "Rule_Delete_Backup_RDS_Prod"
  description = "Delete_Backup_RDS_Prod"
  schedule_expression = "cron(0 6 * * ? *)"
}
resource "aws_cloudwatch_event_target" "Target_Delete_Backup_RDS_Prod" {
  arn = aws_lambda_function.Delete_Backup_RDS_Prod.arn
  rule = aws_cloudwatch_event_rule.Rule_Delete_Backup_RDS_Prod.name
  target_id = "Delete_Backup_RDS_Prod"
}

resource "aws_lambda_permission" "Lambda_Permission_Delete_Backup_RDS_Prod" {
  statement_id = "AllowExecutionFromCloudWatch"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.Delete_Backup_RDS_Prod.function_name
  principal = "events.amazonaws.com"
  source_arn = aws_cloudwatch_event_rule.Rule_Delete_Backup_RDS_Prod.arn
}