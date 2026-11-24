from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .route53_coordinates_model import Route53CoordinatesModel


class Route53GeoProximityLocationModel(BaseModel):
    AWSRegion: StrictStr | None = None
    LocalZoneGroup: StrictStr | None = None
    Coordinates: Route53CoordinatesModel | None = None
    Bias: StrictInt | None = None
