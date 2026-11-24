from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneNameIdentifier(BaseModel):
    name: StrictStr | None = None
    namespace: StrictStr | None = None
