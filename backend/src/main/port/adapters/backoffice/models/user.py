from pydantic import BaseModel


class UserBackofficeModel(BaseModel):
    id: str
    name: str


class UserCreationRequestBody(BaseModel):
    name: str