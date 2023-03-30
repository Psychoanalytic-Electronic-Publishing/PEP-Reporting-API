terraform {
  backend "s3" {
    key = "global/s3/reporting-api-stage.tfstate"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.52.0"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = var.aws_region
}

module "reporting_api" {
  source = "../modules/reporting"
}
