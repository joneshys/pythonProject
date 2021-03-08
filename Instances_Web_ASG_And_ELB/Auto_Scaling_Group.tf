#Creacion del Creacion del autoScaling

resource "aws_autoscaling_group" "Instances_Pool_Web" {
  name = "${var.project_name}_Instances_Pool_Web_"
  max_size = 2
  min_size = 0
  desired_capacity = 1
  launch_configuration = aws_launch_configuration.Instances_Pool_Web.name
  vpc_zone_identifier = [aws_subnet.VPCPrivateSubnetACidrBlock.id, aws_subnet.VPCPrivateSubnetBCidrBlock.id]
  target_group_arns = [aws_lb_target_group.lb_target_group.arn, aws_lb_target_group.lb_target_group_docker.arn]

  tag {
    key = "Name"
    propagate_at_launch = true
    value = "${var.project_name}_Instances_Pool_Web"
  }
}


