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

  env                         = var.env
  stack_name                  = var.stack_name
  github_assignees_data_error = var.github_assignees_data_error
  github_assignees_feedback   = var.github_assignees_feedback
  github_labels               = var.github_labels
  github_private_key          = var.github_private_key
  github_app_id               = var.github_app_id
  github_installation_id      = var.github_installation_id
  github_owner                = var.github_owner
  github_repo                 = var.github_repo
  root_domain                 = var.root_domain
  cors_origin                 = var.cors_origin
  api_domain                  = var.api_domain

}
