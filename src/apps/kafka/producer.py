from aiokafka import AIOKafkaProducer

from src.config import settings


async def init_producer() -> AIOKafkaProducer:
    producer = AIOKafkaProducer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS_URL)
    await producer.start()

    return producer


async def producer_send_one(topic: str, value: any) -> None:
    producer = await init_producer()
    await producer.start()
    await producer.send_and_wait(topic=topic, value=value.encode('utf-8'))
    await producer.stop()
