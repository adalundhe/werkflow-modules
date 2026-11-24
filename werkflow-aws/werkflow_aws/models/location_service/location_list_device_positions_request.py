from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .location_tracking_filter_geometry import LocationTrackingFilterGeometry


class LocationListDevicePositionsRequest(BaseModel):
    TrackerName: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    FilterGeometry: LocationTrackingFilterGeometry | None = None
