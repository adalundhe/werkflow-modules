from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_catalog_entry import GlueCatalogEntry
from .glue_location import GlueLocation
from .glue_mapping_entry import GlueMappingEntry


class GlueGetPlanRequest(BaseModel):
    Mapping: list[GlueMappingEntry]
    Source: GlueCatalogEntry
    Sinks: list[GlueCatalogEntry] | None = None
    Location: GlueLocation | None = None
    Language: Literal['PYTHON', 'SCALA'] | None = None
    AdditionalPlanOptionsMap: dict[StrictStr, StrictStr] | None = None
