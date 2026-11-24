from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .comprehend_tag import ComprehendTag


class ComprehendTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[ComprehendTag]
