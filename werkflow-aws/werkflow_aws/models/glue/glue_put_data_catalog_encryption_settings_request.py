from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_data_catalog_encryption_settings import GlueDataCatalogEncryptionSettings


class GluePutDataCatalogEncryptionSettingsRequest(BaseModel):
    DataCatalogEncryptionSettings: GlueDataCatalogEncryptionSettings
    CatalogId: StrictStr | None = None
