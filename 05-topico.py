import boto3

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
        try:
            topic = self.sns_resource.create_topic(Name=name)
            logger.info("Created topic %s with ARN %s.", name, topic.arn)
        except ClientError:
            logger.exception("Couldn't create topic %s.", name)
            raise
        else:
            return topic

sns_resource = boto3.resource('sns', region_name='us-east-1')

SnsWrapper.create_topic(sns_resource,"ada")

# class SnsWrapper:
#     """Encapsulates Amazon SNS topic and subscription functions."""

#     def __init__(self, sns_resource):
#         """
#         :param sns_resource: A Boto3 Amazon SNS resource.
#         """
#         self.sns_resource = sns_resource


#     @staticmethod
#     def publish_message(topic, message, attributes):
#         """
#         Publishes a message, with attributes, to a topic. Subscriptions can be filtered
#         based on message attributes so that a subscription receives messages only
#         when specified attributes are present.

#         :param topic: The topic to publish to.
#         :param message: The message to publish.
#         :param attributes: The key-value attributes to attach to the message. Values
#                            must be either `str` or `bytes`.
#         :return: The ID of the message.
#         """
#         try:
#             att_dict = {}
#             for key, value in attributes.items():
#                 if isinstance(value, str):
#                     att_dict[key] = {"DataType": "String", "StringValue": value}
#                 elif isinstance(value, bytes):
#                     att_dict[key] = {"DataType": "Binary", "BinaryValue": value}
#             response = topic.publish(Message=message, MessageAttributes=att_dict)
#             message_id = response["MessageId"]
#             logger.info(
#                 "Published message with attributes %s to topic %s.",
#                 attributes,
#                 topic.arn,
#             )
#         except ClientError:
#             logger.exception("Couldn't publish message to topic %s.", topic.arn)
#             raise
#         else:
#             return message_id


