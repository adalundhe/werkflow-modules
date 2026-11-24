from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectoryServiceListTagsForResourceRequest(BaseModel):
    ResourceId: StrictStr
    NextToken: StrictStr | None = None
    Limit: StrictInt | None = None
