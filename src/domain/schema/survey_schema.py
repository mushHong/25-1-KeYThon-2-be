from pydantic import BaseModel, Field
from typing import Dict

class RouteReqPostSurvey(BaseModel):
    answers: Dict[str, str] = Field(title="The survey answers")


class RouteResPostSurvey(BaseModel):
    result: int = Field(title="The response point", ge=0, le=100)


class RouteReqPostTopic(BaseModel):
    point: int = Field(title="The point", ge=0, le=100)
    topic: str = Field(title="The topic")


class RouteResPostTopic(BaseModel):
    articles: Dict[str, str] = Field(title="The articles")
    count: int = Field(title="The count of articles", ge=0)
