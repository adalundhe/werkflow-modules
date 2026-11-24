from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .dms_tag import DMSTag


class DMSListTagsForResourceResponse(BaseModel):
    TagList: list[DMSTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
