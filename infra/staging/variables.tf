variable "env" {
  description = "Environment name"
  default     = "staging"
}

variable "aws_region" {
  description = "AWS region"
  default     = "us-east-1"
}

variable "stack_name" {
  description = "Root name for the stack"
  default     = "pep-reporting-api"
}

variable "github_assignees_data_error" {
  description = "Github assignees for data error issues"
  default     = "jordanallen-dev"
}

variable "github_assignees_feedback" {
  description = "Github assignees for feedback issues"
  default     = "jordanallen-dev"
}

variable "github_labels" {
  description = "Github labels for issues"
  default     = "Client User Issue Reported"
}

variable "github_repo" {
  description = "Github repo for issues"
  default     = "jordanallen-dev/pep-test"
}

variable "github_token" {
  description = "Github token for issues"
  sensitive   = true
}
