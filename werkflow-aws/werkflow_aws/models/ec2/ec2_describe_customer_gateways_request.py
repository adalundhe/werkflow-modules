from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeCustomerGatewaysRequest(BaseModel):
    CustomerGatewayIds: list[StrictStr] | None = None
    Filters: list[EC2FilterModel] | None = None
    DryRun: StrictBool | None = None
