from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeReservedInstancesRequest(BaseModel):
    OfferingClass: Literal['standard', 'convertible'] | None = None
    ReservedInstancesIds: list[StrictStr] | None = None
    DryRun: StrictBool | None = None
    Filters: list[EC2FilterModel] | None = None
    OfferingType: Literal['Heavy Utilization', 'Medium Utilization', 'Light Utilization', 'No Upfront', 'Partial Upfront', 'All Upfront'] | None = None
