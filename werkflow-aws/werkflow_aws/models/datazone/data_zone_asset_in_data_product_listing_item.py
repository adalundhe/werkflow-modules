from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataZoneAssetInDataProductListingItem(BaseModel):
    entityId: StrictStr | None = None
    entityRevision: StrictStr | None = None
    entityType: StrictStr | None = None
