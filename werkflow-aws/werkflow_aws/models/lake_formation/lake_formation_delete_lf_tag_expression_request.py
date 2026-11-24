from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDeleteLFTagExpressionRequest(BaseModel):
    Name: StrictStr
    CatalogId: StrictStr | None = None
