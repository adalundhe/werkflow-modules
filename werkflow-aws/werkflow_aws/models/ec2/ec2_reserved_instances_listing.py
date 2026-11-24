from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_instance_count import EC2InstanceCount
from .ec2_price_schedule import EC2PriceSchedule
from .ec2_tag_model import EC2TagModel


class EC2ReservedInstancesListing(BaseModel):
    ClientToken: StrictStr | None = None
    CreateDate: datetime.datetime | StrictStr | None = None
    InstanceCounts: list[EC2InstanceCount] | None = None
    PriceSchedules: list[EC2PriceSchedule] | None = None
    ReservedInstancesId: StrictStr | None = None
    ReservedInstancesListingId: StrictStr | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    UpdateDate: datetime.datetime | StrictStr | None = None
