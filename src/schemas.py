from pydantic import BaseModel


class ActivityCreate(BaseModel):
    name: str
    description: str
    schedule: str
    max_participants: int


class SignupRequest(BaseModel):
    email: str
