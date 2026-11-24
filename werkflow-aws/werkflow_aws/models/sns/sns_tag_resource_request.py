from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .sns_tag import SNSTag


class SNSTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[SNSTag]
