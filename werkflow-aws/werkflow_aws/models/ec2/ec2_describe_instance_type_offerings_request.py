from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeInstanceTypeOfferingsRequest(BaseModel):
    DryRun: StrictBool | None = None
    LocationType: Literal['region', 'availability-zone', 'availability-zone-id', 'outpost'] | None = None
    Filters: list[EC2FilterModel] | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
