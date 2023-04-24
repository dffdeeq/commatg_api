from pydantic import BaseModel


class BotAddSchema(BaseModel):
    api_id: str
    api_hash: str
    phone_number: str
    two_step_password: str | None
