import json
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers='localhost:9092')
topic = "orders"
message = json.dumps({ "id": 0, "count": 1 })
producer.send(topic, str.encode(message))
producer.flush()
