from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FMSNetworkFirewallMissingFirewallViolation(BaseModel):
    ViolationTarget: StrictStr | None = None
    VPC: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    TargetViolationReason: StrictStr | None = None
