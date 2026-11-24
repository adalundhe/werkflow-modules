from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CostExplorerGetTagsResponse(BaseModel):
    NextPageToken: StrictStr | None = None
    Tags: list[StrictStr] | None = None
    ReturnSize: StrictInt | None = None
    TotalSize: StrictInt | None = None
