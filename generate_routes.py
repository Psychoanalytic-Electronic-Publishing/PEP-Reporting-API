import os.path
import json
import yaml
import re

class RouteGenerator:
    def generate_serverless_route_configs(self, routes_file_path: str, unauthorized_routes_file_path: str):
        yaml_dict = self.build_dictionary(unauthorized_routes_file_path)
        with open(routes_file_path, "w") as file:
            file.truncate(0)
            yaml.dump(yaml_dict, file)

    def build_dictionary(self, unauthorized_routes_file_path: str):
        filename = "information.json"
        #base file content
        yamlDict = dict(
                app = dict(
                handler = 'wsgi_handler.handler',
                events = [
                    {"http": "ANY /"},
                    {"http": "ANY {proxy+}"}
                ]
                )
            )

        #retrieve non protected endpoints
        unauthorized_endpoints = []
        with open(unauthorized_routes_file_path, "r") as file:
            line = file.readline()
            while line:
                lineText = line.strip()
                if not lineText.startswith("#"):
                    unauthorized_endpoints.append(line.strip())
                line = file.readline()

        #open json file to retrieve information
        with open(filename, 'r') as f:
            jsonDict = json.load(f)
            paths = jsonDict["paths"]
            for path in paths:
                for verb in paths[path]:
                    if verb == "parameters":
                        continue
                    events_http_path = re.sub("\{.+\}", "{proxy+}", path.strip("/"))
                    events_http_method = verb
                    events_http = dict(
                        path = events_http_path,
                        method = events_http_method,
                        cors = dict(
                            origin = os.environ.get('ORIGIN'),
                            allowCredentials = "true",
                            headers = ['Content-Type',
                                'Authorization',
                                'X-Amz-Date',
                                'X-Api-Key',
                                'X-Amz-Security-Token',
                                'X-Amz-User-Agent',
                                'client-session',
                                'client-id'
                            ]
                        )
                    )
                    if paths[path][verb]["operationId"] not in unauthorized_endpoints and "*" not in unauthorized_endpoints:
                        events_http["authorizer"] = dict(
                            type = "COGNITO_USER_POOLS",
                            authorizerId = dict(
                                Ref = "ApiGatewayAuthorizer"
                            )
                        )
                    yamlDict['app']['events'].append(dict(http = events_http))
        return yamlDict


