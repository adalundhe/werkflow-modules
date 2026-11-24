from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .acm_tag import ACMTag


class ACMListTagsForResourceResponse(BaseModel):
    Tags: list[ACMTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
