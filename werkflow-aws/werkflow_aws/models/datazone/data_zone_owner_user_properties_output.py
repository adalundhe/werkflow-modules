from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneOwnerUserPropertiesOutput(BaseModel):
    userId: StrictStr | None = None
