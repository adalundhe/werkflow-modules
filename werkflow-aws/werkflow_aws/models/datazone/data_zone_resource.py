from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneResource(BaseModel):
    provider: StrictStr | None = None
    name: StrictStr | None = None
    value: StrictStr | None = None
    type: StrictStr | None = None
