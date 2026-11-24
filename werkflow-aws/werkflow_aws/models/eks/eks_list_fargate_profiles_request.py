from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EKSListFargateProfilesRequest(BaseModel):
    clusterName: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
