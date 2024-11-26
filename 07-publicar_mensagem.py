import boto3
import json
import logger

class SnsWrapper:

    '''Iniciando o sns e obtendo o sns_resource'''
    def __init__(self,sns_resource):
        self.sns_resource = sns_resource

    '''Criando um tópico'''
    def create_topic(self, name):
        topic = self.sns_resource.create_topic(Name=name)
        return topic

    '''Criando assinatura e-mail'''
    def subscribe(self, topic_arn, protocol, endpoint):
        topic = self.sns_resource.Topic(topic_arn)
        subscription = topic.subscribe(
            Protocol=protocol, Endpoint=endpoint, ReturnSubscriptionArn=True
        )
        return subscription

    def add_email_subscription(self, topic_arn, email):
        subscription = self.subscribe(topic_arn, protocol="email", endpoint=email)
        return subscription

    '''publicando mensagem'''
    def publish_multi_message(
        self,topic_arn, subject, default_message, sms_message, email_message
    ):
        topic = self.sns_resource.Topic(topic_arn)
        message = {
            "default": default_message,
            "sms": sms_message,
            "email": email_message,
        }
        response = topic.publish(
            Message=json.dumps(message), Subject=subject, MessageStructure="json"
        )
        message_id = response["MessageId"]
        return message_id



sns_resource = boto3.resource('sns', region_name='us-east-1')
topic_arn = "arn:aws:sns:us-east-1:862147242199:ada"

#Cadastrar um e-mail e confirmar (código comentado pois o e-mail já foi confirmado)
# email = "souzafonseca.gsf@gmail.com"
# SnsWrapper(sns_resource).add_email_subscription(topic_arn, email)

SnsWrapper(sns_resource).publish_multi_message(topic_arn,"mensagem da aula","","","mensagem de e-mail enviada com sucesso")
