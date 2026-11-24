from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .el_bv2_matcher import ELBv2Matcher


class ELBv2ModifyTargetGroupRequest(BaseModel):
    TargetGroupArn: StrictStr
    HealthCheckProtocol: Literal['HTTP', 'HTTPS', 'TCP', 'TLS', 'UDP', 'TCP_UDP', 'GENEVE', 'QUIC', 'TCP_QUIC'] | None = None
    HealthCheckPort: StrictStr | None = None
    HealthCheckPath: StrictStr | None = None
    HealthCheckEnabled: StrictBool | None = None
    HealthCheckIntervalSeconds: StrictInt | None = None
    HealthCheckTimeoutSeconds: StrictInt | None = None
    HealthyThresholdCount: StrictInt | None = None
    UnhealthyThresholdCount: StrictInt | None = None
    Matcher: ELBv2Matcher | None = None
