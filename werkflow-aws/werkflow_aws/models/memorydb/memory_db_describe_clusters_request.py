from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class MemoryDBDescribeClustersRequest(BaseModel):
    ClusterName: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    ShowShardDetails: StrictBool | None = None
