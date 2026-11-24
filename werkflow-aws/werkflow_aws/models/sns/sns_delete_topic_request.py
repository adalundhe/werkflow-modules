from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SNSDeleteTopicRequest(BaseModel):
    TopicArn: StrictStr
