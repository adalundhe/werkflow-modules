from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetDataCatalogEncryptionSettingsRequest(BaseModel):
    CatalogId: StrictStr | None = None
