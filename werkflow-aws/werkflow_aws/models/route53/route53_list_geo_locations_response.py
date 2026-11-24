from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .route53_geo_location_details import Route53GeoLocationDetails


class Route53ListGeoLocationsResponse(BaseModel):
    GeoLocationDetailsList: list[Route53GeoLocationDetails] | None = None
    IsTruncated: StrictBool | None = None
    NextContinentCode: StrictStr | None = None
    NextCountryCode: StrictStr | None = None
    NextSubdivisionCode: StrictStr | None = None
    MaxItems: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
