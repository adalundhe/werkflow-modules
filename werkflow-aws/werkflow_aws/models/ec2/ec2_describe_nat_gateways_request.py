from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeNatGatewaysRequest(BaseModel):
    DryRun: StrictBool | None = None
    Filter: list[EC2FilterModel] | None = None
    MaxResults: StrictInt | None = None
    NatGatewayIds: list[StrictStr] | None = None
    NextToken: StrictStr | None = None
