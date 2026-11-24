from __future__ import annotations
from typing import Any
from pydantic import BaseModel


class GluePutDataCatalogEncryptionSettingsResponse(BaseModel):
    ResponseMetadata: dict[str, Any] | None = None
