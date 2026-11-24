from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53ListReusableDelegationSetsRequest(BaseModel):
    Marker: StrictStr | None = None
    MaxItems: StrictStr | None = None
