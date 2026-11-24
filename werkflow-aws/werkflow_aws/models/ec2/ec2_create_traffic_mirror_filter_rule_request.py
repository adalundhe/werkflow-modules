from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_tag_specification_model import EC2TagSpecificationModel
from .ec2_traffic_mirror_port_range_request import EC2TrafficMirrorPortRangeRequest


class EC2CreateTrafficMirrorFilterRuleRequest(BaseModel):
    TrafficMirrorFilterId: StrictStr
    TrafficDirection: Literal['ingress', 'egress']
    RuleNumber: StrictInt
    RuleAction: Literal['accept', 'reject']
    DestinationCidrBlock: StrictStr
    SourceCidrBlock: StrictStr
    DestinationPortRange: EC2TrafficMirrorPortRangeRequest | None = None
    SourcePortRange: EC2TrafficMirrorPortRangeRequest | None = None
    Protocol: StrictInt | None = None
    Description: StrictStr | None = None
    DryRun: StrictBool | None = None
    ClientToken: StrictStr | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
