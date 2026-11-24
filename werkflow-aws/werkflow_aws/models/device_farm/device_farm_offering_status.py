from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .device_farm_offering import DeviceFarmOffering


class DeviceFarmOfferingStatus(BaseModel):
    type: StrictStr | None = None
    offering: DeviceFarmOffering | None = None
    quantity: StrictInt | None = None
    effectiveOn: datetime.datetime | StrictStr | None = None
