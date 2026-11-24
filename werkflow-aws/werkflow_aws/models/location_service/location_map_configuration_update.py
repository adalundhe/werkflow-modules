from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LocationMapConfigurationUpdate(BaseModel):
    PoliticalView: StrictStr | None = None
    CustomLayers: list[StrictStr] | None = None
