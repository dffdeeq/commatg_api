import json

from fastapi import APIRouter

from src.apps.bot.schemas import BotAddSchema
from src.apps.kafka.consumer import init_consumer
from src.apps.kafka.producer import init_producer
from src.apps.kafka.producer import producer_send_one

router = APIRouter(prefix='/bot',
                   tags=['Bot'])


@router.post('/add')
async def add_bot(bot: BotAddSchema):
    print('start api')
    await producer_send_one(topic='try_add_bot', value=bot.json())
    print('sent')

    return {'status': 'Trying to create a bot, check result at /bot_status'}


@router.get('/bot_status/{api_id}')
async def get_status_of_bot(api_id: str):
    await producer_send_one(topic='bot_status_request', value=api_id)

    consumer = await init_consumer('bot_status_response')
    try:
        async for msg in consumer:
            response = msg.value
            return {'status': response}
    finally:
        await consumer.stop()

    return {'status': 'fail'}


@router.post('/code/{api_id}')
async def confirm_code_bot(api_id: str, code: str):
    await producer_send_one(topic='bot_code', value=json.dumps({'api_id': api_id, 'code': code}))
    return {'status': 'Trying to confirm code, check result at /bot_status'}


@router.post('/{api_id}/{command}')
async def send_command_to_bot(api_id: str, command: str, arg1: str):
    await producer_send_one(topic=api_id, value=json.dumps({'command': command, 'arg1': arg1}))
    return {'status': 'Command sent to bot, check status at /status'}
