from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .ec2_recurring_charge import EC2RecurringCharge
from .ec2_tag_model import EC2TagModel


class EC2ReservedInstances(BaseModel):
    CurrencyCode: StrictStr | None = None
    InstanceTenancy: StrictStr | None = None
    OfferingClass: StrictStr | None = None
    OfferingType: StrictStr | None = None
    RecurringCharges: list[EC2RecurringCharge] | None = None
    Scope: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
    AvailabilityZoneId: StrictStr | None = None
    ReservedInstancesId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    Start: datetime.datetime | StrictStr | None = None
    End: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    UsagePrice: StrictFloat | StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    InstanceCount: StrictInt | None = None
    ProductDescription: StrictStr | None = None
    State: StrictStr | None = None
