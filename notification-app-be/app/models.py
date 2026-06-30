from pydantic import BaseModel

class Notification(BaseModel):
    id: int
    title: str
    message: str
    user: str