from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneConfiguration(BaseModel):
    classification: StrictStr | None = None
    properties: dict[StrictStr, StrictStr] | None = None
