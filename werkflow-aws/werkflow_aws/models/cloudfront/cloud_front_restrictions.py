from __future__ import annotations
from pydantic import BaseModel
from .cloud_front_geo_restriction import CloudFrontGeoRestriction


class CloudFrontRestrictions(BaseModel):
    GeoRestriction: CloudFrontGeoRestriction | None = None
