from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneCreateEnvironmentProfilePolicyGrantDetail(BaseModel):
    domainUnitId: StrictStr | None = None
