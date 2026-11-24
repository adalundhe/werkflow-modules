from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListHealthChecksRequest(BaseModel):
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
