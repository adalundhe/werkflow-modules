from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .neptune_tag import NeptuneTag


class NeptuneAddTagsToResourceRequest(BaseModel):
    ResourceName: StrictStr
    Tags: list[NeptuneTag]
