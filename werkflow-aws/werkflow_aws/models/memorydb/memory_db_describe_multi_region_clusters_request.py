from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class MemoryDBDescribeMultiRegionClustersRequest(BaseModel):
    MultiRegionClusterName: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    ShowClusterDetails: StrictBool | None = None
