from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EKSListAssociatedAccessPoliciesRequest(BaseModel):
    clusterName: StrictStr
    principalArn: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
