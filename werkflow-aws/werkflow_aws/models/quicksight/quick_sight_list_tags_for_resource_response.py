from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .quick_sight_tag import QuickSightTag


class QuickSightListTagsForResourceResponse(BaseModel):
    Tags: list[QuickSightTag] | None = None
    RequestId: StrictStr | None = None
    Status: StrictInt | None = None
    ResponseMetadata: dict[str, Any] | None = None
