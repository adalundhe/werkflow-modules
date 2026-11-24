from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailResourceReceivingAccess(BaseModel):
    name: StrictStr | None = None
    resourceType: StrictStr | None = None
