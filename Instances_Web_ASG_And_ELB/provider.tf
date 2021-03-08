#Se obtiene las credenciales para el despligue en la cuenta indicada

provider "aws" {
  shared_credentials_file = "C:\\Users\\jose.benitez\\.aws"
  profile = "Test_Packer"
  region = "us-east-1"
}