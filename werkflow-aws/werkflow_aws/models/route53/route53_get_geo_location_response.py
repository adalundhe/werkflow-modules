from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .route53_geo_location_details import Route53GeoLocationDetails


class Route53GetGeoLocationResponse(BaseModel):
    GeoLocationDetails: Route53GeoLocationDetails | None = None
    ResponseMetadata: dict[str, Any] | None = None
