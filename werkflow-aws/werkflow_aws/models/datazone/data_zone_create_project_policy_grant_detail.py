from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneCreateProjectPolicyGrantDetail(BaseModel):
    includeChildDomainUnits: StrictBool | None = None
