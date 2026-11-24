from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ARCClusterEndpoint(BaseModel):
    Endpoint: StrictStr | None = None
    Region: StrictStr | None = None
