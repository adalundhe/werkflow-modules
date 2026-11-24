from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DataZoneLineageSyncOutput(BaseModel):
    lineageJobId: StrictStr | None = None
    timezone: StrictStr | None = None
    enabled: StrictBool | None = None
    schedule: StrictStr | None = None
