from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DataSyncListTagsForResourceRequest(BaseModel):
    ResourceArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
