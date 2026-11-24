from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetCatalogImportStatusRequest(BaseModel):
    CatalogId: StrictStr | None = None
