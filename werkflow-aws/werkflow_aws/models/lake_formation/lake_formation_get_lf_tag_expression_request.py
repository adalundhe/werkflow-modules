from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationGetLFTagExpressionRequest(BaseModel):
    Name: StrictStr
    CatalogId: StrictStr | None = None
