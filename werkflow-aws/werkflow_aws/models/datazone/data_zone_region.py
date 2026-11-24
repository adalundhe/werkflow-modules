from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneRegion(BaseModel):
    regionName: StrictStr | None = None
    regionNamePath: StrictStr | None = None
