from __future__ import annotations
from pydantic import BaseModel
from .glue_catalog_entry import GlueCatalogEntry
from .glue_location import GlueLocation


class GlueGetMappingRequest(BaseModel):
    Source: GlueCatalogEntry
    Sinks: list[GlueCatalogEntry] | None = None
    Location: GlueLocation | None = None
