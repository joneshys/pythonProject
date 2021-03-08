#Se obtiene las credenciales para el despligue en la cuenta indicada

provider "aws" {
  shared_credentials_file = "C:\\Users\\jose.benitez\\.aws"
  profile = "QXSSDDATLANTICOTEST"
  region = "us-west-2"
}