from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .kendra_tag import KendraTag


class KendraListTagsForResourceResponse(BaseModel):
    Tags: list[KendraTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
