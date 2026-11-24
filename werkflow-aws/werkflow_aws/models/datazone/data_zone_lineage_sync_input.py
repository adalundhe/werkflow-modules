from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneLineageSyncInput(BaseModel):
    enabled: StrictBool
    timezone: StrictStr | None = None
    schedule: StrictStr | None = None
