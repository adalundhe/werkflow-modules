from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .el_bv2_matcher import ELBv2Matcher


class ELBv2TargetGroup(BaseModel):
    TargetGroupArn: StrictStr | None = None
    TargetGroupName: StrictStr | None = None
    Protocol: StrictStr | None = None
    Port: StrictInt | None = None
    VpcId: StrictStr | None = None
    HealthCheckProtocol: StrictStr | None = None
    HealthCheckPort: StrictStr | None = None
    HealthCheckEnabled: StrictBool | None = None
    HealthCheckIntervalSeconds: StrictInt | None = None
    HealthCheckTimeoutSeconds: StrictInt | None = None
    HealthyThresholdCount: StrictInt | None = None
    UnhealthyThresholdCount: StrictInt | None = None
    HealthCheckPath: StrictStr | None = None
    Matcher: ELBv2Matcher | None = None
    LoadBalancerArns: list[StrictStr] | None = None
    TargetType: StrictStr | None = None
    ProtocolVersion: StrictStr | None = None
    IpAddressType: StrictStr | None = None
    TargetControlPort: StrictInt | None = None
