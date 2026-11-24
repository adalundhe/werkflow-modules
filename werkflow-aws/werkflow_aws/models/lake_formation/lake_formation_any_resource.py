from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationAnyResource(BaseModel):
    CatalogId: StrictStr | None = None
    ResourceType: StrictStr | None = None
