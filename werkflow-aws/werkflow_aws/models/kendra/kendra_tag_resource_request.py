from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kendra_tag import KendraTag


class KendraTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[KendraTag]
