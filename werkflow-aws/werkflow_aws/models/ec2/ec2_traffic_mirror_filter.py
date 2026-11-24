from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_tag_model import EC2TagModel
from .ec2_traffic_mirror_filter_rule import EC2TrafficMirrorFilterRule


class EC2TrafficMirrorFilter(BaseModel):
    TrafficMirrorFilterId: StrictStr | None = None
    IngressFilterRules: list[EC2TrafficMirrorFilterRule] | None = None
    EgressFilterRules: list[EC2TrafficMirrorFilterRule] | None = None
    NetworkServices: list[StrictStr] | None = None
    Description: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
