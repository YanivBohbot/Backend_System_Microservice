import json
import logging
from kafka import KafkaConsumer , KafkaProducer


logging.basicConfig(level=logging.INFO)


ORDER_KAFKA_TOPIC="order-details"
ORDER_PROCESSED_KAFKA_TOPIC = "order_processed"
BOOT_STRAP_SERVER= "kafka-local.orders-microservice.svc.cluster.local:9092"

# consumer for consuming the data from kafka hub and then we can process the data 
# we create a topic which ORDER_KAFKA_TOPIC
consumer = KafkaConsumer(
    ORDER_KAFKA_TOPIC,
     bootstrap_servers=BOOT_STRAP_SERVER
)


# producer
producer = KafkaProducer(bootsstrap_server=BOOT_STRAP_SERVER)


if __name__ == '__main__':
    logging.info("Started processing transactions...")
    while True:
        for message in consumer:
            consumed_message = json.loads(message.value.decode("utf-8"))

            username = consumed_message["username"]
            qty = consumed_message["quantity"]
            price = consumed_message["price"]
            total_cost = round(float(qty * price), 2)

            data = {
                "username": username,
                "order_id": consumed_message["order_id"],
                "email": consumed_message["email"],
                "total_cost": total_cost
            }
            logging.info(f"Successful transactions sent ... {data}")
            # send message to processed order topic
            producer.send(ORDER_PROCESSED_KAFKA_TOPIC, json.dumps(data).encode("utf-8"))