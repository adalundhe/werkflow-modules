from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .swf_resource_tag import SWFResourceTag


class SWFTagResourceRequest(BaseModel):
    resourceArn: StrictStr
    tags: list[SWFResourceTag]
