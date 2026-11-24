from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDeleteLFTagRequest(BaseModel):
    TagKey: StrictStr
    CatalogId: StrictStr | None = None
