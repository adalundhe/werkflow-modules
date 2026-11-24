from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudFrontGeoRestrictionCustomization(BaseModel):
    RestrictionType: StrictStr | None = None
    Locations: list[StrictStr] | None = None
