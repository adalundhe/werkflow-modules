from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .fms_tag import FMSTag


class FMSListTagsForResourceResponse(BaseModel):
    TagList: list[FMSTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
