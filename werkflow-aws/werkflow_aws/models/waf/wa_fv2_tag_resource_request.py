from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_tag import WAFv2Tag


class WAFv2TagResourceRequest(BaseModel):
    ResourceARN: StrictStr
    Tags: list[WAFv2Tag]
