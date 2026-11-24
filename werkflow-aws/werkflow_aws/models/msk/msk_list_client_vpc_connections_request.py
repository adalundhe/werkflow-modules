from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKListClientVpcConnectionsRequest(BaseModel):
    ClusterArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
