from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_coordinates import Route53Coordinates


class Route53GeoProximityLocation(BaseModel):
    AWSRegion: StrictStr | None = None
    LocalZoneGroup: StrictStr | None = None
    Coordinates: Route53Coordinates | None = None
    Bias: StrictInt | None = None
