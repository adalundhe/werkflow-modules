from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_connectivity_filter import IoTConnectivityFilter
from .io_t_geo_location_target import IoTGeoLocationTarget


class IoTIndexingFilter(BaseModel):
    namedShadowNames: list[StrictStr] | None = None
    geoLocations: list[IoTGeoLocationTarget] | None = None
    connectivity: IoTConnectivityFilter | None = None
