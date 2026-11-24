from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .swf_resource_tag import SWFResourceTag


class SWFListTagsForResourceResponse(BaseModel):
    tags: list[SWFResourceTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
