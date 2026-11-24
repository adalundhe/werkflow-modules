from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .security_lake_tag import SecurityLakeTag


class SecurityLakeListTagsForResourceResponse(BaseModel):
    tags: list[SecurityLakeTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
