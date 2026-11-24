from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationCreateLFTagRequest(BaseModel):
    TagKey: StrictStr
    TagValues: list[StrictStr]
    CatalogId: StrictStr | None = None
