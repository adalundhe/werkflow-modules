from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneRejectSubscriptionRequestRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    decisionComment: StrictStr | None = None
