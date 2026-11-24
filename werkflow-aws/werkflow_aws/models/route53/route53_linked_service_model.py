from __future__ import annotations
from pydantic import BaseModel, StrictStr


class Route53LinkedServiceModel(BaseModel):
    ServicePrincipal: StrictStr | None = None
    Description: StrictStr | None = None
