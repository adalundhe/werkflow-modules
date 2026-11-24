from __future__ import annotations
from pydantic import BaseModel, StrictBool


class DataZoneCreateGlossaryPolicyGrantDetail(BaseModel):
    includeChildDomainUnits: StrictBool | None = None
