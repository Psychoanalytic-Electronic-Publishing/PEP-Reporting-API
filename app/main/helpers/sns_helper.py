import os
import boto3
import json
from botocore.exceptions import ClientError
from flask import current_app as app

sns_client = boto3.client('sns')

class SnsHelper:
    @staticmethod
    def send_message_to_topic(topic_arn, subject, email_message, sms_message):
        try:
            sns_client.publish(
                TargetArn=topic_arn,
                Message=json.dumps(
                    {
                        'default': json.dumps(email_message),
                        'sms': sms_message,
                        'email': email_message
                    }),
                Subject=subject,
                MessageStructure='json'
            )
        except ClientError as e:
            app.logger.error(e)

