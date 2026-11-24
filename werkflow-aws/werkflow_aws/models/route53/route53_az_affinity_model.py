from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53AZAffinityModel(BaseModel):
    LocationType: StrictStr | None = None
    LocationId: StrictStr | None = None
