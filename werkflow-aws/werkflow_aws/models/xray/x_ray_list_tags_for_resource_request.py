from __future__ import annotations
from pydantic import BaseModel, StrictStr


class XRayListTagsForResourceRequest(BaseModel):
    ResourceARN: StrictStr
    NextToken: StrictStr | None = None
