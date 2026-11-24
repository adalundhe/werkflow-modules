from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .comprehend_tag import ComprehendTag


class ComprehendListTagsForResourceResponse(BaseModel):
    ResourceArn: StrictStr | None = None
    Tags: list[ComprehendTag] | None = None
    ResponseMetadata: dict[str, Any] | None = None
