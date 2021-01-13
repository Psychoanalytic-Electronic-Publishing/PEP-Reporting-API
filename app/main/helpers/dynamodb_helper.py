import os
import boto3
import time
from app.main import app
from app.main.config import Config

dynamodb = boto3.resource('dynamodb')

class DynamoDbHelper:
    @staticmethod
    def save_data_error(data_error):
        table = dynamodb.Table(app.config[Config.DYNAMODB_TABLE_DATA_ERROR])
        resp = table.put_item(
            Item={
                'id': data_error['id'],
                'date_created': data_error['date_created'],
                'date_modified': data_error['date_modified'],
                'is_active': data_error['is_active'],
                'username': data_error['username'],
                'email': data_error['email'],
                'full_name': data_error['full_name'],
                'problem_text': data_error['problem_text'],
                'corrected_text': data_error['corrected_text'],
                'url_problem_page': data_error['url_problem_page'],
                'additional_info': data_error['additional_info'],
                'is_author_publisher': data_error['is_author_publisher'],
                'has_original_copy': data_error['has_original_copy']
            }
        )
        return resp

    @staticmethod
    def get_data_error(id):
        table = dynamodb.Table(app.config[Config.DYNAMODB_TABLE_DATA_ERROR])
        resp = table.get_item(Key={'id': id})
        return resp['Item']