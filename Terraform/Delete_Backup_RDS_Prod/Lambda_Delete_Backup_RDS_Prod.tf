provider "aws" {
  region = "us-east-1"
  profile = "QXSSDDSABANETAPROD"
}

provider "archive" {}

data "archive_file" "zip" {
  source_file = "Delete_Backup_RDS_Prod.py"
  output_path = "Delete_Backup_RDS_Prod.zip"
  type = "zip"
}

resource "aws_lambda_function" "Delete_Backup_RDS_Prod" {
  function_name = "Delete_Backup_RDS_Prod"

  filename = data.archive_file.zip.output_path
  source_code_hash = data.archive_file.zip.output_base64sha256

  role = aws_iam_role.Role_Access_Lambda.arn
  handler = "Delete_Backup_RDS_Prod.lambda_handler"
  runtime = "python3.8"
  timeout = "121"

  environment {
    variables = {
      greeting = "Hello"
    }
  }
}
