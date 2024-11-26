import boto3
import logger
from botocore.exceptions import ClientError

class SnsWrapper:
    """Encapsulates Amazon SNS topic and subscription functions."""

    def __init__(self, sns_resource):
        """
        :param sns_resource: A Boto3 Amazon SNS resource.
        """
        self.sns_resource = sns_resource


    def create_topic(self, name):
        """
        Creates a notification topic.

        :param name: The name of the topic to create.
        :return: The newly created topic.
        """
        topic = self.sns_resource.create_topic(Name=name)
        return topic

sns_resource = boto3.resource('sns', region_name='us-east-1')

SnsWrapper(sns_resource).create_topic("ada")
