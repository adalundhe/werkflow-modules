from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .location_forecast_geofence_events_device_state import LocationForecastGeofenceEventsDeviceState


class LocationForecastGeofenceEventsRequest(BaseModel):
    CollectionName: StrictStr
    DeviceState: LocationForecastGeofenceEventsDeviceState
    TimeHorizonMinutes: StrictFloat | StrictInt | None = None
    DistanceUnit: Literal['Kilometers', 'Miles'] | None = None
    SpeedUnit: Literal['KilometersPerHour', 'MilesPerHour'] | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
