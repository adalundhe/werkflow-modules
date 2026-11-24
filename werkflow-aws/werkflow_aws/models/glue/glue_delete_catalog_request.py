from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDeleteCatalogRequest(BaseModel):
    CatalogId: StrictStr
