from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_data_catalog_encryption_settings import GlueDataCatalogEncryptionSettings


class GlueGetDataCatalogEncryptionSettingsResponse(BaseModel):
    DataCatalogEncryptionSettings: GlueDataCatalogEncryptionSettings | None = None
    ResponseMetadata: dict[str, Any] | None = None
