from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDataLocationResource(BaseModel):
    CatalogId: StrictStr | None = None
    ResourceArn: StrictStr | None = None
