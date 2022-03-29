from kafka import KafkaProducer
from django.conf import settings

import json
import sys
import os

import logging

logger = logging.getLogger("kafka")
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.ERROR)


def send_output(data, topic):
    producer = KafkaProducer(
        bootstrap_servers=settings.KAFKA_HOST,
        sasl_plain_username=settings.KAFKA_USERNAME,
        sasl_plain_password=settings.KAFKA_PASSWORD,
        sasl_mechanism="PLAIN",
        security_protocol="SASL_PLAINTEXT",
    )
    producer.send(topic=topic, value=json.dumps(data).encode("utf-8"))
    producer.flush()
