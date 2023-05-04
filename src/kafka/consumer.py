from aiokafka import AIOKafkaConsumer

from .config import settings


async def init_consumer(
        topic
):
    consumer = AIOKafkaConsumer(
        topic,
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS_URL)
    await consumer.start()

    return consumer
