from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_tag import QuickSightTag


class QuickSightTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    Tags: list[QuickSightTag]
