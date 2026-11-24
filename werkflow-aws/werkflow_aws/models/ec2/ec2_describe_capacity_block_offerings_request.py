from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .ec2_capacity_block_instance_type_preference import EC2CapacityBlockInstanceTypePreference


class EC2DescribeCapacityBlockOfferingsRequest(BaseModel):
    CapacityDurationHours: StrictInt
    DryRun: StrictBool | None = None
    InstanceType: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    StartDateRange: datetime.datetime | StrictStr | None = None
    EndDateRange: datetime.datetime | StrictStr | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    UltraserverType: StrictStr | None = None
    UltraserverCount: StrictInt | None = None
    AllAvailabilityZones: StrictBool | None = None
    InstanceTypePreferences: list[EC2CapacityBlockInstanceTypePreference] | None = None
