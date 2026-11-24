from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LambdaListTagsResponse(BaseModel):
    Tags: dict[StrictStr, StrictStr] | None = None
