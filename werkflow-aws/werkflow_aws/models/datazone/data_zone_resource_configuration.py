from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneResourceConfiguration(BaseModel):
    identifier: StrictStr | None = None
    name: StrictStr | None = None
    description: StrictStr | None = None
    region: StrictStr | None = None
    parameters: dict[StrictStr, StrictStr] | None = None
