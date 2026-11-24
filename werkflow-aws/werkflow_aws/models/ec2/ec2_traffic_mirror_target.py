from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2TrafficMirrorTarget(BaseModel):
    TrafficMirrorTargetId: StrictStr | None = None
    NetworkInterfaceId: StrictStr | None = None
    NetworkLoadBalancerArn: StrictStr | None = None
    Type: StrictStr | None = None
    Description: StrictStr | None = None
    OwnerId: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    GatewayLoadBalancerEndpointId: StrictStr | None = None
