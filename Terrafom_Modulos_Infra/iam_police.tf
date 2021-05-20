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
  name = "PoliceEC2DeleteBackup"
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

resource "aws_iam_user_policy_attachment" "User_Policy_Attachment" {
  policy_arn = aws_iam_policy.Police_EC2_Delete_Backup.arn
  user = "NlcHoxuWr69aC"
}