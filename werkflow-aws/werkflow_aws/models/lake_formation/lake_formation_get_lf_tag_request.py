from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationGetLFTagRequest(BaseModel):
    TagKey: StrictStr
    CatalogId: StrictStr | None = None
