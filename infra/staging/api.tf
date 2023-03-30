moved {
  from = aws_api_gateway_rest_api.api_gateway
  to   = module.reporting_api.aws_api_gateway_rest_api.api_gateway
}

moved {
  from = aws_api_gateway_deployment.api_deployment
  to   = module.reporting_api.aws_api_gateway_deployment.api_deployment
}
