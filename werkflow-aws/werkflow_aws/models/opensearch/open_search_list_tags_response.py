from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_tag import OpenSearchTag


class OpenSearchListTagsResponse(BaseModel):
    TagList: list[OpenSearchTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
