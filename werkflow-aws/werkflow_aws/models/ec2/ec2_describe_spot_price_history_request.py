from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_filter_model import EC2FilterModel


class EC2DescribeSpotPriceHistoryRequest(BaseModel):
    AvailabilityZoneId: StrictStr | None = None
    DryRun: StrictBool | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    InstanceTypes: list[StrictStr] | None = None
    ProductDescriptions: list[StrictStr] | None = None
    Filters: list[EC2FilterModel] | None = None
    AvailabilityZone: StrictStr | None = None
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
