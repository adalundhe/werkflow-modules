from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_catalog import GlueCatalog


class GlueGetCatalogResponse(BaseModel):
    Catalog: GlueCatalog | None = None
    ResponseMetadata: dict[str, Any] | None = None
