import json
from kafka import KafkaConsumer


inventory = {
	0: {
		"name": "bread",
		"stock": 5
	},
	1: {
		"name": "eggs",
		"stock": 3
	}
}

topic = KafkaConsumer("orders")
for message in topic:
	order = json.loads(message.value)
	item = inventory[order["id"]]
	try:
		new_stock = item["stock"] - order["count"]
		if new_stock < 0:
			raise Exception(f"insufficient stock! {item['name']}: {item['stock']}, order: {order['count']}")
		item["stock"] = new_stock
		print(item)
	except Exception as e:
		print(e)
