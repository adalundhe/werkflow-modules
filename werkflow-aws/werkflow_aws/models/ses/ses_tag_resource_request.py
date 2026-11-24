from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ses_tag import SESTag


class SESTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[SESTag]
