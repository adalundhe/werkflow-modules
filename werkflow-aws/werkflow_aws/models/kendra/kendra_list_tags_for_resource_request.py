from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
