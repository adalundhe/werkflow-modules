from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ec2_availability_zone_geography import EC2AvailabilityZoneGeography
from .ec2_availability_zone_message import EC2AvailabilityZoneMessage
from .ec2_availability_zone_sub_geography import EC2AvailabilityZoneSubGeography


class EC2AvailabilityZone(BaseModel):
    OptInStatus: StrictStr | None = None
    Messages: list[EC2AvailabilityZoneMessage] | None = None
    RegionName: StrictStr | None = None
    ZoneName: StrictStr | None = None
    ZoneId: StrictStr | None = None
    GroupName: StrictStr | None = None
    NetworkBorderGroup: StrictStr | None = None
    ZoneType: StrictStr | None = None
    ParentZoneName: StrictStr | None = None
    ParentZoneId: StrictStr | None = None
    GroupLongName: StrictStr | None = None
    Geography: list[EC2AvailabilityZoneGeography] | None = None
    SubGeography: list[EC2AvailabilityZoneSubGeography] | None = None
    State: StrictStr | None = None
