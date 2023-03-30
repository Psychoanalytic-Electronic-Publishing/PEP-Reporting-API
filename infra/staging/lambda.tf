moved {
  from = aws_lambda_permission.allow_api_data_error
  to   = module.reporting_api.aws_lambda_permission.allow_api_data_error
}

moved {
  from = aws_lambda_permission.allow_api_data_feedback
  to   = module.reporting_api.aws_lambda_permission.allow_api_data_feedback
}

moved {
  from = module.data_error_lambda
  to   = module.reporting_api.module.data_error_lambda
}

moved {
  from = module.feedback_lambda
  to   = module.reporting_api.module.feedback_lambda
}
