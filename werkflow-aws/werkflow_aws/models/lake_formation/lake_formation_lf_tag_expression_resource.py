from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationLFTagExpressionResource(BaseModel):
    CatalogId: StrictStr | None = None
    Name: StrictStr | None = None
