moved {
  from = aws_api_gateway_domain_name.reporting
  to   = module.reporting_api.aws_api_gateway_domain_name.reporting
}

moved {
  from = aws_api_gateway_base_path_mapping.mapping
  to   = module.reporting_api.aws_api_gateway_base_path_mapping.mapping
}
