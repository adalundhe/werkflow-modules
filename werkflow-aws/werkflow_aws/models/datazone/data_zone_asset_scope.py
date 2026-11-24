from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAssetScope(BaseModel):
    assetId: StrictStr | None = None
    filterIds: list[StrictStr] | None = None
    status: StrictStr | None = None
    scopeName: StrictStr | None = None
    errorMessage: StrictStr | None = None
