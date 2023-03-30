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

variable "github_private_key" {
  description = "Github private key for app"
  sensitive   = true
}

variable "github_app_id" {
  description = "Github app id"
  default     = 306306
}

variable "github_installation_id" {
  description = "Github installation id"
  default     = 35322311
}

variable "github_owner" {
  description = "Github owner"
  default     = "Psychoanalytic-Electronic-Publishing"
}

variable "github_repo" {
  description = "Github repo for issues"
  default     = "pep-reporting-api"
}

variable "root_domain" {
  description = "Root domain name"
  default     = "pep-web.org"
}

variable "cors_origin" {
  description = "CORS origin"
  default     = "https://stage.pep-web.org"
}

variable "api_domain" {
  description = "Domain name"
  default     = "stage-report.pep-web.org"
}
