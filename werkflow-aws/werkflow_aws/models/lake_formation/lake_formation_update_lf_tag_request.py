from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationUpdateLFTagRequest(BaseModel):
    TagKey: StrictStr
    CatalogId: StrictStr | None = None
    TagValuesToDelete: list[StrictStr] | None = None
    TagValuesToAdd: list[StrictStr] | None = None
