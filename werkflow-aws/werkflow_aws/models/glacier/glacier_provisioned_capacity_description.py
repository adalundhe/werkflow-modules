from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlacierProvisionedCapacityDescription(BaseModel):
    CapacityId: StrictStr | None = None
    StartDate: StrictStr | None = None
    ExpirationDate: StrictStr | None = None
