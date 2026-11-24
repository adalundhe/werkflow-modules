from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeClientVpnAuthorizationRulesRequest(BaseModel):
    ClientVpnEndpointId: StrictStr
    DryRun: StrictBool | None = None
    NextToken: StrictStr | None = None
    Filters: list[EC2FilterModel] | None = None
    MaxResults: StrictInt | None = None
