from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .route53_az_affinity_location_type import Route53AZAffinityLocationType


class Route53AZAffinity(BaseModel):
    LocationType: Route53AZAffinityLocationType | None = None
    LocationId: StrictStr | None = None
