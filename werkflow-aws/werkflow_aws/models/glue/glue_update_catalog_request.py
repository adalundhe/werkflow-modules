from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_catalog_input import GlueCatalogInput


class GlueUpdateCatalogRequest(BaseModel):
    CatalogId: StrictStr
    CatalogInput: GlueCatalogInput
