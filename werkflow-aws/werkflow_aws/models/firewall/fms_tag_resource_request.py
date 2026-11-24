from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .fms_tag import FMSTag


class FMSTagResourceRequest(BaseModel):
    ResourceArn: StrictStr
    TagList: list[FMSTag]
