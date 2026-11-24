from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53HostedZoneFailureReasons(BaseModel):
    AcceleratedRecovery: StrictStr | None = None
