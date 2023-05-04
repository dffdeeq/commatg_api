from decouple import config


class Settings:
    KAFKA_HOST = config('KAFKA_HOST', cast=str, default='localhost')
    KAFKA_PORT = config('KAFKA_PORT', cast=int, default=9092)
    KAFKA_BOOTSTRAP_SERVERS_URL = f'{KAFKA_HOST}:{KAFKA_PORT}'


settings = Settings()
