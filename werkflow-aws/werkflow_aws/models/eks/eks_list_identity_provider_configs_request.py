from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EKSListIdentityProviderConfigsRequest(BaseModel):
    clusterName: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
