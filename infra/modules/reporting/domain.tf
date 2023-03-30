resource "aws_api_gateway_domain_name" "reporting" {
  certificate_arn = "arn:aws:acm:us-east-1:547758924192:certificate/0ef7fa01-6a14-4342-a5cd-a3a55719b160"
  domain_name     = var.api_domain
  tags = {
    stage = var.env
    stack = var.stack_name
  }
}

resource "aws_api_gateway_base_path_mapping" "mapping" {
  api_id      = aws_api_gateway_rest_api.api_gateway.id
  stage_name  = aws_api_gateway_deployment.api_deployment.stage_name
  domain_name = aws_api_gateway_domain_name.reporting.domain_name
}
