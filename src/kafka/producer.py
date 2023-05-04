from aiokafka import AIOKafkaProducer

from .config import settings


async def init_producer() -> AIOKafkaProducer:
    producer = AIOKafkaProducer(
        bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS_URL)
    await producer.start()

    return producer


async def producer_send_one(
        topic: str,
        value: any
):
    print('producer_send_one func')
    producer = await init_producer()
    print(producer, type(producer))
    await producer.start()
    print('producer start...')
    await producer.send_and_wait(topic=topic, value=value.encode('utf-8'))
    print('producer sent')
    await producer.stop()
    print('producer stop')
