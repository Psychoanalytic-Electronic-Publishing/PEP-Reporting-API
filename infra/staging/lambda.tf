module "data_error_lambda" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "4.9.0"

  function_name           = "${var.stack_name}-data-error-handler-${var.env}"
  source_path             = "../../app"
  handler                 = "main/controller/data_error_controller.handler"
  runtime                 = "python3.8"
  timeout                 = 29
  ignore_source_code_hash = true

  tags = {
    stage = var.env
    stack = var.stack_name
  }

  environment_variables = {
    "GITHUB_ASSIGNEES" = var.github_assignees_data_error
    "GITHUB_LABELS"    = var.github_labels
    "GITHUB_REPO"      = var.github_repo
    "GITHUB_TOKEN"     = var.github_token
  }
}

module "feedback_lambda" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "4.9.0"

  function_name           = "${var.stack_name}-feedback-handler-${var.env}"
  source_path             = "../../app"
  handler                 = "main/controller/feedback_controller.handler"
  runtime                 = "python3.8"
  timeout                 = 29
  ignore_source_code_hash = true

  tags = {
    stage = var.env
    stack = var.stack_name
  }

  environment_variables = {
    "GITHUB_ASSIGNEES" = var.github_assignees_feedback
    "GITHUB_LABELS"    = var.github_labels
    "GITHUB_REPO"      = var.github_repo
    "GITHUB_TOKEN"     = var.github_token
  }
}
