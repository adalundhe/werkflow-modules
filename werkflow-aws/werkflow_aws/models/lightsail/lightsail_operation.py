from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .lightsail_resource_location import LightsailResourceLocation


class LightsailOperation(BaseModel):
    id: StrictStr | None = None
    resourceName: StrictStr | None = None
    resourceType: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    location: LightsailResourceLocation | None = None
    isTerminal: StrictBool | None = None
    operationDetails: StrictStr | None = None
    operationType: StrictStr | None = None
    status: StrictStr | None = None
    statusChangedAt: datetime.datetime | StrictStr | None = None
    errorCode: StrictStr | None = None
    errorDetails: StrictStr | None = None
