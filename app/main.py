from kafka import KafkaConsumer
import json

# Kafka consumer to read messages from the topic
consumer = KafkaConsumer(
    'dbserver1.test.users',  # The topic name (change it based on your MySQL table)
    bootstrap_servers=['localhost:9093'],
    group_id='debezium-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)

# Consume messages from the Kafka topic
for message in consumer:
    print(f"Captured change: {message.value}")