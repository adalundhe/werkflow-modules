from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class FSxDescribeFileCachesRequest(BaseModel):
    FileCacheIds: list[StrictStr] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
