module "package_error" {

  source  = "terraform-aws-modules/lambda/aws"
  version = "2.31.0"

  source_path = [
    {
      path = "../../app",
      commands = [
        "pip install --platform manylinux2014_x86_64 --implementation cp --python 3.8 --only-binary=:all: --upgrade -t . cryptography",
        "pip install -r requirements.txt -t .",
        ":zip"
      ]
  }]
  runtime                  = "python3.8"
  create_function          = false
  recreate_missing_package = true
}

module "data_error_lambda" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "4.9.0"

  function_name          = "${var.stack_name}-data-error-handler-${var.env}"
  local_existing_package = module.package_error.local_filename
  create_package         = false
  publish                = true

  handler = "main/controller/data_error_controller.handler"
  runtime = "python3.8"
  timeout = 29

  tags = {
    stage = var.env
    stack = var.stack_name
  }
  environment_variables = {
    "GITHUB_ASSIGNEES"       = var.github_assignees_data_error
    "GITHUB_LABELS"          = var.github_labels
    "GITHUB_OWNER"           = var.github_owner
    "GITHUB_REPO"            = var.github_repo
    "GITHUB_PRIVATE_KEY"     = var.github_private_key
    "GITHUB_APP_ID"          = var.github_app_id
    "GITHUB_INSTALLATION_ID" = var.github_installation_id
    "CORS_ORIGINS"           = var.cors_origin
  }
}

resource "aws_lambda_permission" "allow_api_data_error" {
  statement_id  = "${var.stack_name}-allow-api-data-error-${var.env}"
  action        = "lambda:InvokeFunction"
  function_name = module.data_error_lambda.lambda_function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.api_gateway.execution_arn}/*/*/*"
}

module "package_feedback" {

  source  = "terraform-aws-modules/lambda/aws"
  version = "2.31.0"

  source_path = [
    {
      path = "../../app",
      commands = [
        "pip install --platform manylinux2014_x86_64 --implementation cp --python 3.8 --only-binary=:all: --upgrade -t . cryptography",
        "pip install -r requirements.txt -t .",
        ":zip"
      ]
  }]
  runtime                  = "python3.8"
  create_function          = false
  recreate_missing_package = true
}


module "feedback_lambda" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "4.9.0"

  function_name          = "${var.stack_name}-feedback-handler-${var.env}"
  local_existing_package = module.package_feedback.local_filename
  create_package         = false
  publish                = true

  handler = "main/controller/feedback_controller.handler"
  runtime = "python3.8"
  timeout = 29

  tags = {
    stage = var.env
    stack = var.stack_name
  }

  environment_variables = {
    "GITHUB_ASSIGNEES"       = var.github_assignees_feedback
    "GITHUB_LABELS"          = var.github_labels
    "GITHUB_OWNER"           = var.github_owner
    "GITHUB_REPO"            = var.github_repo
    "GITHUB_PRIVATE_KEY"     = var.github_private_key
    "GITHUB_APP_ID"          = var.github_app_id
    "GITHUB_INSTALLATION_ID" = var.github_installation_id
    "CORS_ORIGIN"            = var.cors_origin
  }
}

module "package_test" {

  source  = "terraform-aws-modules/lambda/aws"
  version = "2.31.0"

  source_path = [
    {
      path = "../../app",
      commands = [
        "pip install --platform manylinux2014_x86_64 --implementation cp --python 3.8 --only-binary=:all: --upgrade -t . cryptography",
        "pip install -r requirements.txt -t .",
        ":zip"
      ]
  }]
  runtime                  = "python3.8"
  create_function          = false
  recreate_missing_package = true
}


module "test_lambda" {
  source  = "terraform-aws-modules/lambda/aws"
  version = "4.9.0"

  function_name          = "${var.stack_name}-test-${var.env}"
  local_existing_package = module.package_test.local_filename
  create_package         = false
  publish                = true

  handler = "main/controller/feedback_controller.handler"
  runtime = "python3.8"
  timeout = 29

  tags = {
    stage = var.env
    stack = var.stack_name
  }

  environment_variables = {
    "GITHUB_ASSIGNEES"       = var.github_assignees_feedback
    "GITHUB_LABELS"          = var.github_labels
    "GITHUB_OWNER"           = var.github_owner
    "GITHUB_REPO"            = var.github_repo
    "GITHUB_PRIVATE_KEY"     = var.github_private_key
    "GITHUB_APP_ID"          = var.github_app_id
    "GITHUB_INSTALLATION_ID" = var.github_installation_id
    "CORS_ORIGIN"            = var.cors_origin
  }
}



resource "aws_lambda_permission" "allow_api_data_feedback" {
  statement_id  = "${var.stack_name}-allow-api-feedback-${var.env}"
  action        = "lambda:InvokeFunction"
  function_name = module.feedback_lambda.lambda_function_name
  principal     = "apigateway.amazonaws.com"
  source_arn    = "${aws_api_gateway_rest_api.api_gateway.execution_arn}/*/*/*"
}

