from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .neptune_tag import NeptuneTag


class NeptuneListTagsForResourceResponse(BaseModel):
    TagList: list[NeptuneTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
