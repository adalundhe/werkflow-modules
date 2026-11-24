from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .sns_tag import SNSTag


class SNSListTagsForResourceResponse(BaseModel):
    Tags: list[SNSTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
