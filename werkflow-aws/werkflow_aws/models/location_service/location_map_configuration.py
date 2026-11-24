from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationMapConfiguration(BaseModel):
    Style: StrictStr | None = None
    PoliticalView: StrictStr | None = None
    CustomLayers: list[StrictStr] | None = None
