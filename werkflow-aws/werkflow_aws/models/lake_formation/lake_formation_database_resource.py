from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationDatabaseResource(BaseModel):
    CatalogId: StrictStr | None = None
    Name: StrictStr | None = None
