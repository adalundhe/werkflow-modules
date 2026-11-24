from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr


class LocationForecastedEvent(BaseModel):
    EventId: StrictStr | None = None
    GeofenceId: StrictStr | None = None
    IsDeviceInGeofence: StrictBool | None = None
    NearestDistance: StrictFloat | StrictInt | None = None
    EventType: StrictStr | None = None
    ForecastedBreachTime: datetime.datetime | StrictStr | None = None
    GeofenceProperties: dict[StrictStr, StrictStr] | None = None
