from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeAvailabilityZonesRequest(BaseModel):
    ZoneNames: list[StrictStr] | None = None
    ZoneIds: list[StrictStr] | None = None
    AllAvailabilityZones: StrictBool | None = None
    DryRun: StrictBool | None = None
    Filters: list[EC2FilterModel] | None = None
