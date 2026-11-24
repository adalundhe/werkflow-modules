from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeReservedInstancesOfferingsRequest(BaseModel):
    AvailabilityZone: StrictStr | None = None
    IncludeMarketplace: StrictBool | None = None
    InstanceType: StrictStr | None = None
    MaxDuration: StrictInt | None = None
    MaxInstanceCount: StrictInt | None = None
    MinDuration: StrictInt | None = None
    OfferingClass: Literal['standard', 'convertible'] | None = None
    ProductDescription: Literal['Linux/UNIX', 'Linux/UNIX (Amazon VPC)', 'Windows', 'Windows (Amazon VPC)'] | None = None
    ReservedInstancesOfferingIds: list[StrictStr] | None = None
    AvailabilityZoneId: StrictStr | None = None
    DryRun: StrictBool | None = None
    Filters: list[EC2FilterModel] | None = None
    InstanceTenancy: Literal['default', 'dedicated', 'host'] | None = None
    OfferingType: Literal['Heavy Utilization', 'Medium Utilization', 'Light Utilization', 'No Upfront', 'Partial Upfront', 'All Upfront'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
