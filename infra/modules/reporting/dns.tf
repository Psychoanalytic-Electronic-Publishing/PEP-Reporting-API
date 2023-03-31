data "aws_route53_zone" "pep_web" {
  name         = var.root_domain
  private_zone = false
}

resource "aws_route53_record" "web_alias" {
  zone_id = data.aws_route53_zone.pep_web.zone_id
  name    = var.api_domain
  type    = "A"

  alias {
    name                   = aws_api_gateway_domain_name.reporting.cloudfront_domain_name
    zone_id                = aws_api_gateway_domain_name.reporting.cloudfront_zone_id
    evaluate_target_health = false
  }
}
