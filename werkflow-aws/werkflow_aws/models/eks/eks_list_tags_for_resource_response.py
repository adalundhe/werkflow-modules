from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EKSListTagsForResourceResponse(BaseModel):
    tags: dict[StrictStr, StrictStr] | None = None
