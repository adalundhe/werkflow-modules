from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .open_search_serverless_tag import OpenSearchServerlessTag


class OpenSearchServerlessListTagsForResourceResponse(BaseModel):
    tags: list[OpenSearchServerlessTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
