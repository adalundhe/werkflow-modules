from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_resource_location import LightsailResourceLocation


class LightsailStaticIp(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    supportCode: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    ipAddress: StrictStr | None = None
    attachedTo: StrictStr | None = None
    isAttached: StrictBool | None = None
