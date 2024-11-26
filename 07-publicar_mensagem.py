import boto3
import json
import logger

class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""

    def __init__(self, sns_resource):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sns_resource

    @staticmethod
    def publish_multi_message(
        topic, subject, default_message, sms_message, email_message
    ):
        message = {
            "default": default_message,
            "sms": sms_message,
            "email": email_message,
        }
        response = topic.publish(
            Message=json.dumps(message), Subject=subject, MessageStructure="json"
        )
        message_id = response["MessageId"]
        logger.info("Published multi-format message to topic %s.", topic.arn)

        return message_id

sns_resource = boto3.resource('sns', region_name='us-east-1')
SnsWrapper(sns_resource).publish_multi_message("ada","mensagem da aula","x","y","z")

