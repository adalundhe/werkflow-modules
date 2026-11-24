from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ec2_capacity_manager_tag_dimension import EC2CapacityManagerTagDimension


class EC2CapacityManagerDimension(BaseModel):
    ResourceRegion: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    AccountId: StrictStr | None = None
    AccountName: StrictStr | None = None
    InstanceFamily: StrictStr | None = None
    InstanceType: StrictStr | None = None
    InstancePlatform: StrictStr | None = None
    ReservationArn: StrictStr | None = None
    ReservationId: StrictStr | None = None
    ReservationType: StrictStr | None = None
    ReservationCreateTimestamp: datetime.datetime | StrictStr | None = None
    ReservationStartTimestamp: datetime.datetime | StrictStr | None = None
    ReservationEndTimestamp: datetime.datetime | StrictStr | None = None
    ReservationEndDateType: StrictStr | None = None
    Tenancy: StrictStr | None = None
    ReservationState: StrictStr | None = None
    ReservationInstanceMatchCriteria: StrictStr | None = None
    ReservationUnusedFinancialOwner: StrictStr | None = None
    Tags: list[EC2CapacityManagerTagDimension] | None = None
