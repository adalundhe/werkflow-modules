from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .wa_fv2_tag import WAFv2Tag


class WAFv2TagInfoForResource(BaseModel):
    ResourceARN: StrictStr | None = None
    TagList: list[WAFv2Tag] | None = None
