from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKListClusterOperationsV2Request(BaseModel):
    ClusterArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
