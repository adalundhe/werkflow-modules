from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneRevokeSubscriptionRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    retainPermissions: StrictBool | None = None
