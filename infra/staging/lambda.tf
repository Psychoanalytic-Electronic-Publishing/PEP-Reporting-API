module "data_error_lambda" {
  source = "terraform-aws-modules/lambda/aws"

  function_name = "${var.stack_name}-data-error-handler-${var.env}"
  source_path   = "../../app"
  handler       = "main/controller/data_error_controller.handler"
  runtime       = "python3.8"
  timeout       = 29
  memory_size   = 3072


  tags = {
    stage = var.env
    stack = var.stack_name
  }

  environment_variables = {
    "GITHUB_ASSIGNEES_DATAERROR" = "jordanallen-dev"
    "GITHUB_ASSIGNEES_FEEDBACK"  = "jordanallen-dev"
    "GITHUB_LABELS"              = "Client User Issue Reported"
    "GITHUB_REPO"                = "jordanallen-dev/pep-test"
    "GITHUB_TOKEN"               = "..."
  }
}
