from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CloudFrontGeoRestriction(BaseModel):
    RestrictionType: StrictStr | None = None
    Quantity: StrictInt | None = None
    Items: list[StrictStr] | None = None
