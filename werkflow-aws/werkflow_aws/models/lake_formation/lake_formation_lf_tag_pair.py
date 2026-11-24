from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationLFTagPair(BaseModel):
    CatalogId: StrictStr | None = None
    TagKey: StrictStr | None = None
    TagValues: list[StrictStr] | None = None
