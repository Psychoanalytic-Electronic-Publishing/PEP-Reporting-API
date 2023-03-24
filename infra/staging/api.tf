locals {
  options = {
    responses = {
      200 = {
        description = "200 response",
        headers = {
          Access-Control-Allow-Origin = {
            schema = {
              type = "string"
            }
          },
          Access-Control-Allow-Methods = {
            schema = {
              type = "string"
            }
          },
          Access-Control-Allow-Credentials = {
            schema = {
              type = "string"
            }
          },
          Access-Control-Allow-Headers = {
            schema = {
              type = "string"
            }
          }
        },
        content = {}
      }
    },
    x-amazon-apigateway-integration = {
      responses = {
        default = {
          statusCode = 200,
          responseParameters = {
            "method.response.header.Access-Control-Allow-Credentials" = "'true'",
            "method.response.header.Access-Control-Allow-Methods"     = "'OPTIONS,POST'",
            "method.response.header.Access-Control-Allow-Headers"     = "'Content-Type,Authorization,X-Amz-Date,X-Api-Key,X-Amz-Security-Token,X-Amz-User-Agent,client-session,client-id,x-pep-auth'",
            "method.response.header.Access-Control-Allow-Origin"      = "'${var.cors_origin}'"
          }
          responseTemplates = {
            "application/json" = ""
          }
        }
      },
      requestTemplates = {
        "application/json" = "{statusCode:200}"
      },
      passthroughBehavior = "when_no_match",
      contentHandling     = "CONVERT_TO_TEXT",
      type                = "mock"
    }
  }
}

resource "aws_api_gateway_rest_api" "api_gateway" {
  name        = "${var.stack_name}-${var.env}-api"
  description = "API Gateway for ${var.stack_name} ${var.env}"
  tags = {
    stage = var.env
    stack = var.stack_name
  }
  body = jsonencode({
    openapi = "3.0.1"
    info = {
      title   = "example"
      version = "1.0"
    }
    paths = {
      "/data-errors" = {
        post = {
          x-amazon-apigateway-integration = {
            httpMethod           = "POST"
            payloadFormatVersion = "1.0"
            type                 = "AWS_PROXY"
            uri                  = module.data_error_lambda.lambda_function_invoke_arn
          }
        },
        options = local.options
      }
      "/feedback" = {
        post = {
          x-amazon-apigateway-integration = {
            httpMethod           = "POST"
            payloadFormatVersion = "1.0"
            type                 = "AWS_PROXY"
            uri                  = module.feedback_lambda.lambda_function_invoke_arn
          }
        },
        options = local.options
      },
    }
  })
}

resource "aws_api_gateway_deployment" "api_deployment" {
  rest_api_id = aws_api_gateway_rest_api.api_gateway.id
  triggers = {
    redeployment = sha1(jsonencode(aws_api_gateway_rest_api.api_gateway.body))
  }
  lifecycle {
    create_before_destroy = true
  }
  stage_name = "v1"
}
