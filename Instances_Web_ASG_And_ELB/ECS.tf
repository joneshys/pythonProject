#Creacion del ECR, y del ECS(Cluster, Taks, Service)
resource "aws_ecr_repository" "dockerTest" {
  name = "dockertest"
  image_tag_mutability = "MUTABLE"
  image_scanning_configuration {
    scan_on_push = true
  }
}

