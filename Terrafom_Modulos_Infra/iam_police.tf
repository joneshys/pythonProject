# Acceso a Bastion
resource "aws_iam_role" "Role_Access_Bastion" {
  name = "RoleAccessBastion"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}
resource "aws_iam_policy" "Police_Access_Bastion" {
  name = "Police_Access_Bastion"
  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "AccessBastion",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "ec2:DescribeSecurityGroups",
                "ec2:RevokeSecurityGroupIngress",
                "ec2:AuthorizeSecurityGroupIngress"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}
resource "aws_iam_role_policy_attachment" "Attachment_Access_Bastion" {
  policy_arn = aws_iam_policy.Police_Access_Bastion.arn
  role = aws_iam_role.Role_Access_Bastion.name
}
resource "aws_iam_user_policy_attachment" "User_Policy_Attachment_Access_Bastion" {
  policy_arn = aws_iam_policy.Police_Access_Bastion.arn
  user = "NlcHoxuWr69aC"
}

##########################################################

#Encendido de ambientes Pre
resource "aws_iam_role" "Role_Ignition_StepFunction" {
  name = "RoleIgnitionStepFunction"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "states.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}
resource "aws_iam_policy" "Police_Ignition_StepFunction" {
  name = "Police_Ignition_StepFunction"
  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "StartStepFunction",
            "Effect": "Allow",
            "Action": [
                "states:ListStateMachines",
                "states:StartExecution"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}
resource "aws_iam_role_policy_attachment" "Attachment_Ignition_StepFunction" {
  policy_arn = aws_iam_policy.Police_Ignition_StepFunction.arn
  role = aws_iam_role.Role_Ignition_StepFunction.name
}
resource "aws_iam_user_policy_attachment" "User_Policy_Attachment_Ignition_StepFunction" {
  policy_arn = aws_iam_policy.Police_Ignition_StepFunction.arn
  user = "NlcHoxuWr69aC"
}

#############################################################

# Eliminación de los backup de las instancias
resource "aws_iam_role" "Role_EC2_Delete_Backup" {
  name = "RoleEC2DeleteBackup"
  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "ec2.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}
resource "aws_iam_policy" "Police_EC2_Delete_Backup" {
  name = "Police_EC2_Delete_Backup"
  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": ["ec2:DescribeInstances","ec2:DeregisterImage"],
            "Resource": "*"
        }
    ]
}
EOF
}
resource "aws_iam_role_policy_attachment" "Attachment_EC2_Delete_Backup" {
  policy_arn = aws_iam_policy.Police_EC2_Delete_Backup.arn
  role = aws_iam_role.Role_EC2_Delete_Backup.name
}
resource "aws_iam_user_policy_attachment" "User_Policy_Attachment_Delete_Backup_EC2" {
  policy_arn = aws_iam_policy.Police_EC2_Delete_Backup.arn
  user = "NlcHoxuWr69aC"
}
##########################################################################

# Eliminación de los backup de las RDS
resource "aws_iam_role" "Role_RDS_Delete_Backup" {
  name = "RoleRDSDeleteBackup"
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
resource "aws_iam_policy" "Police_RDS_Delete_Backup" {
  name = "Police_RDS_Delete_Backup"
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
resource "aws_iam_role_policy_attachment" "Attachment_RDS_Delete_Backup" {
  policy_arn = aws_iam_policy.Police_RDS_Delete_Backup.arn
  role = aws_iam_role.Role_RDS_Delete_Backup.name
}
resource "aws_iam_user_policy_attachment" "User_Policy_AttachmentDelete_Backup_RDS" {
  policy_arn = aws_iam_policy.Police_RDS_Delete_Backup.arn
  user = "NlcHoxuWr69aC"
}
##########################################################################

# Lambda = Creación de lambada para Actualización Route53 de las IPs de las instancias
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
                "arn:aws:logs:us-east-1:949375136131:log-group:/aws/lambda/Upgrade_IPServer_ON_IPRoute53:*"
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
resource "aws_iam_policy" "Policy_Test_Upgrade_IPServer_ON_IPRoute53" {
  name = "Policy_Test_Upgrade_IPServer_ON_IPRoute53"
  policy = <<EOF
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "VisualEditor0",
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeInstances",
                "route53:ListHostedZones",
                "route53:ListResourceRecordSets",
                "route53:ChangeResourceRecordSets",
                "route53:ChangeResourceRecordSets"
            ],
            "Resource": "*"
        }
    ]
}
EOF
}
resource "aws_iam_role_policy_attachment" "Attachment_Test_Upgrade_IPServer_ON_IPRoute53" {
  policy_arn = aws_iam_policy.Policy_Test_Upgrade_IPServer_ON_IPRoute53.arn
  role = aws_iam_role.Role_Access_Lambda.name
}

