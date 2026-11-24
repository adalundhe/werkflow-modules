from __future__ import annotations
from pydantic import BaseModel, StrictStr


class MediaStoreListTagsForResourceRequest(BaseModel):
    Resource: StrictStr
