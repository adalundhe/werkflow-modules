from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_traffic_mirror_port_range_request import EC2TrafficMirrorPortRangeRequest


class EC2ModifyTrafficMirrorFilterRuleRequest(BaseModel):
    TrafficMirrorFilterRuleId: StrictStr
    TrafficDirection: Literal['ingress', 'egress'] | None = None
    RuleNumber: StrictInt | None = None
    RuleAction: Literal['accept', 'reject'] | None = None
    DestinationPortRange: EC2TrafficMirrorPortRangeRequest | None = None
    SourcePortRange: EC2TrafficMirrorPortRangeRequest | None = None
    Protocol: StrictInt | None = None
    DestinationCidrBlock: StrictStr | None = None
    SourceCidrBlock: StrictStr | None = None
    Description: StrictStr | None = None
    RemoveFields: list[Literal['destination-port-range', 'source-port-range', 'protocol', 'description']] | None = None
    DryRun: StrictBool | None = None
