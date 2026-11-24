from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .route53_location_summary import Route53LocationSummary


class Route53ListCidrLocationsResponse(BaseModel):
    NextToken: StrictStr | None = None
    CidrLocations: list[Route53LocationSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
