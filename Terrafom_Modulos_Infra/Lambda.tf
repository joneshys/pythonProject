provider "archive" {}

data "archive_file" "zip" {
  source_file = "Upgrade_IPServer_ON_IPRoute53.py"
  output_path = "Upgrade_IPServer_ON_IPRoute53.zip"
  type = "zip"
}

resource "aws_lambda_function" "Upgrade_IPServer_ON_IPRoute53" {
  function_name = "Upgrade_IPServer_ON_IPRoute53"

  filename = data.archive_file.zip.output_path
  source_code_hash = data.archive_file.zip.output_base64sha256

  role = aws_iam_role.Role_Access_Lambda.arn
  handler = "Upgrade_IPServer_ON_IPRoute53.lambda_handler"
  runtime = "python3.8"
  timeout = "121"

  environment {
    variables = {
      greeting = "Hello"
    }
  }
}
