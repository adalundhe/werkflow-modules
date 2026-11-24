from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .lightsail_resource_location import LightsailResourceLocation


class LightsailSetupHistoryResource(BaseModel):
    name: StrictStr | None = None
    arn: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    resourceType: StrictStr | None = None
