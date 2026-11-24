from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53HostedZoneFailureReasonsModel(BaseModel):
    AcceleratedRecovery: StrictStr | None = None
