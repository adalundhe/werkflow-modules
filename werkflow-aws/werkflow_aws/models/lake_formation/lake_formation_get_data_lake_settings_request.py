from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationGetDataLakeSettingsRequest(BaseModel):
    CatalogId: StrictStr | None = None
