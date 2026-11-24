from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .f_sx_tag import FSxTag


class FSxTagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[FSxTag]
