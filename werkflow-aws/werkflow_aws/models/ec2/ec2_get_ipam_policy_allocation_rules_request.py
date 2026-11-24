from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2GetIpamPolicyAllocationRulesRequest(BaseModel):
    IpamPolicyId: StrictStr
    DryRun: StrictBool | None = None
    Filters: list[EC2FilterModel] | None = None
    Locale: StrictStr | None = None
    ResourceType: Literal['alb', 'eip', 'rds', 'rnat', 'lambda-network-connector', 'igw-firewall'] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
