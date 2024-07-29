from pydantic import BaseModel
from typing import List


class Event(BaseModel):
    id: int
    title: str
    image: str
    description: str
    tags: List[str]
    location: str

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Meeting of the smart guys",
                "image": "https://test.com",
                "description": "Very good meeting",
                "tags": ["python", "fastapi", "book", "launch"],
                "location": "Moscow"
            }
        }