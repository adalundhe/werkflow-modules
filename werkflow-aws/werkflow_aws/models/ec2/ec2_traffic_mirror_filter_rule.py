from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_traffic_mirror_port_range import EC2TrafficMirrorPortRange


class EC2TrafficMirrorFilterRule(BaseModel):
    TrafficMirrorFilterRuleId: StrictStr | None = None
    TrafficMirrorFilterId: StrictStr | None = None
    TrafficDirection: StrictStr | None = None
    RuleNumber: StrictInt | None = None
    RuleAction: StrictStr | None = None
    Protocol: StrictInt | None = None
    DestinationPortRange: EC2TrafficMirrorPortRange | None = None
    SourcePortRange: EC2TrafficMirrorPortRange | None = None
    DestinationCidrBlock: StrictStr | None = None
    SourceCidrBlock: StrictStr | None = None
    Description: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
