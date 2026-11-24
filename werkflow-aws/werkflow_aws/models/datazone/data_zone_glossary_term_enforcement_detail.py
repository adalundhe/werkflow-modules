from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneGlossaryTermEnforcementDetail(BaseModel):
    requiredGlossaryTermIds: list[StrictStr] | None = None
