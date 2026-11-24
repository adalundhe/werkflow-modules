from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .q_business_tag import QBusinessTag


class QBusinessListTagsForResourceResponse(BaseModel):
    tags: list[QBusinessTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
