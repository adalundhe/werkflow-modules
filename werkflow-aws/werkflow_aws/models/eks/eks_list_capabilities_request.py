from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EKSListCapabilitiesRequest(BaseModel):
    clusterName: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
