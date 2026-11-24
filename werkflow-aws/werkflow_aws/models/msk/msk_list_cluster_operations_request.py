from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MSKListClusterOperationsRequest(BaseModel):
    ClusterArn: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
