from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectListSecurityProfileApplicationsRequest(BaseModel):
    SecurityProfileId: StrictStr
    InstanceId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
