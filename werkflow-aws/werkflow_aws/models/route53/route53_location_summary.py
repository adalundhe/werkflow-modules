from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53LocationSummary(BaseModel):
    LocationName: StrictStr | None = None
