from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EKSListUpdatesRequest(BaseModel):
    name: StrictStr
    nodegroupName: StrictStr | None = None
    addonName: StrictStr | None = None
    capabilityName: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
