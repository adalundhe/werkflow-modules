from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class Route53AliasTarget(BaseModel):
    HostedZoneId: StrictStr | None = None
    DNSName: StrictStr | None = None
    EvaluateTargetHealth: StrictBool | None = None
