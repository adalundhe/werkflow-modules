from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAssetTypesForRule(BaseModel):
    selectionMode: StrictStr | None = None
    specificAssetTypes: list[StrictStr] | None = None
