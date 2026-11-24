from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_catalog_input import GlueCatalogInput


class GlueCreateCatalogRequest(BaseModel):
    Name: StrictStr
    CatalogInput: GlueCatalogInput
    Tags: dict[StrictStr, StrictStr] | None = None
