from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKListClustersV2Request(BaseModel):
    ClusterNameFilter: StrictStr | None = None
    ClusterTypeFilter: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
