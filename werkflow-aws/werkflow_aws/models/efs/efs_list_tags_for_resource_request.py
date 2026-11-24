from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EFSListTagsForResourceRequest(BaseModel):
    ResourceId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
