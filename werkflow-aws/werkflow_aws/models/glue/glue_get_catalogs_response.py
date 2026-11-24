from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_catalog import GlueCatalog


class GlueGetCatalogsResponse(BaseModel):
    CatalogList: list[GlueCatalog] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
