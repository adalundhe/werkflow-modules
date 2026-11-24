from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_failure_cause import DataZoneFailureCause


class DataZoneUpdateSubscriptionGrantStatusRequest(BaseModel):
    domainIdentifier: StrictStr
    identifier: StrictStr
    assetIdentifier: StrictStr
    status: Literal['GRANT_PENDING', 'REVOKE_PENDING', 'GRANT_IN_PROGRESS', 'REVOKE_IN_PROGRESS', 'GRANTED', 'REVOKED', 'GRANT_FAILED', 'REVOKE_FAILED']
    failureCause: DataZoneFailureCause | None = None
    targetName: StrictStr | None = None
