from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ses_tag import SESTag


class SESListTagsForResourceResponse(BaseModel):
    Tags: list[SESTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
