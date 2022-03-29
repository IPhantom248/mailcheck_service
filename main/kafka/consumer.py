# -*- coding: utf-8 -*-
from kafka import KafkaConsumer
import json
import sys
import os
import django
import traceback

# Инициализируем django
sys.path.append(os.getcwd())
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "main.settings")
django.setup()

# from api.models import Model1, Model2...
# from main.kafka.producer import send_output
from django.conf import settings

import logging
logger = logging.getLogger('kafka')
logger.addHandler(logging.StreamHandler(sys.stdout))
logger.setLevel(logging.ERROR)


class ConsumerThread:
    def readData(self):
        self.consumer = KafkaConsumer(
            bootstrap_servers=settings.KAFKA_HOST,
            sasl_plain_username=settings.KAFKA_USERNAME,
            sasl_plain_password=settings.KAFKA_PASSWORD,
            sasl_mechanism='PLAIN',
            security_protocol='SASL_PLAINTEXT',
            consumer_timeout_ms=1000,
            enable_auto_commit=False,
            group_id=settings.KAFKA_GROUP
        )
        self.consumer.subscribe('app_consumer_topic')
        self.run(self.consumer)

    def process_msg(self, msg):
        print("Received message value %s" % msg.value)

    def run(self, consumer):
        try:
            while True:
                msg_pack = consumer.poll(0.1)
                if not msg_pack:
                    continue
                for tp, messages in msg_pack.items():
                    for message in messages:
                        self.process_msg(message)

        except KeyboardInterrupt:
            print("Detected Keyboard Interrupt. Cancelling.")
            pass

        finally:
            consumer.close()

sandbox_consumer = ConsumerThread()
sandbox_consumer.readData()
