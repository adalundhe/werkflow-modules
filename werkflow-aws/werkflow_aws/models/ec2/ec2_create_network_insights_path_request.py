from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_path_request_filter import EC2PathRequestFilter
from .ec2_tag_specification_model import EC2TagSpecificationModel


class EC2CreateNetworkInsightsPathRequest(BaseModel):
    Source: StrictStr
    Protocol: Literal['tcp', 'udp']
    ClientToken: StrictStr
    SourceIp: StrictStr | None = None
    DestinationIp: StrictStr | None = None
    Destination: StrictStr | None = None
    DestinationPort: StrictInt | None = None
    TagSpecifications: list[EC2TagSpecificationModel] | None = None
    DryRun: StrictBool | None = None
    FilterAtSource: EC2PathRequestFilter | None = None
    FilterAtDestination: EC2PathRequestFilter | None = None
