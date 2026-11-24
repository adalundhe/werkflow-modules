from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_catalog_import_status import GlueCatalogImportStatus


class GlueGetCatalogImportStatusResponse(BaseModel):
    ImportStatus: GlueCatalogImportStatus | None = None
    ResponseMetadata: dict[str, Any] | None = None
