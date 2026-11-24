from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53CidrRoutingConfigModel(BaseModel):
    CollectionId: StrictStr | None = None
    LocationName: StrictStr | None = None
