from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .el_bv2_matcher import ELBv2Matcher
from .el_bv2_tag import ELBv2Tag


class ELBv2CreateTargetGroupRequest(BaseModel):
    Name: StrictStr
    Protocol: Literal['HTTP', 'HTTPS', 'TCP', 'TLS', 'UDP', 'TCP_UDP', 'GENEVE', 'QUIC', 'TCP_QUIC'] | None = None
    ProtocolVersion: StrictStr | None = None
    Port: StrictInt | None = None
    VpcId: StrictStr | None = None
    HealthCheckProtocol: Literal['HTTP', 'HTTPS', 'TCP', 'TLS', 'UDP', 'TCP_UDP', 'GENEVE', 'QUIC', 'TCP_QUIC'] | None = None
    HealthCheckPort: StrictStr | None = None
    HealthCheckEnabled: StrictBool | None = None
    HealthCheckPath: StrictStr | None = None
    HealthCheckIntervalSeconds: StrictInt | None = None
    HealthCheckTimeoutSeconds: StrictInt | None = None
    HealthyThresholdCount: StrictInt | None = None
    UnhealthyThresholdCount: StrictInt | None = None
    Matcher: ELBv2Matcher | None = None
    TargetType: Literal['instance', 'ip', 'lambda', 'alb'] | None = None
    Tags: list[ELBv2Tag] | None = None
    IpAddressType: Literal['ipv4', 'ipv6'] | None = None
    TargetControlPort: StrictInt | None = None
