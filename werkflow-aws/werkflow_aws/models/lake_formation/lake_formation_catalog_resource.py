from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationCatalogResource(BaseModel):
    Id: StrictStr | None = None
