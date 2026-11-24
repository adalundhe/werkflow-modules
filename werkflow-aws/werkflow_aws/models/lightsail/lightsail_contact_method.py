from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lightsail_resource_location import LightsailResourceLocation
from .lightsail_tag import LightsailTag


class LightsailContactMethod(BaseModel):
    contactEndpoint: StrictStr | None = None
    status: StrictStr | None = None
    protocol: StrictStr | None = None
    name: StrictStr | None = None
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
    supportCode: StrictStr | None = None
    tags: list[LightsailTag] | None = None
