from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .location_forecasted_event import LocationForecastedEvent


class LocationForecastGeofenceEventsResponse(BaseModel):
    ForecastedEvents: list[LocationForecastedEvent] | None = None
    NextToken: StrictStr | None = None
    DistanceUnit: StrictStr | None = None
    SpeedUnit: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
