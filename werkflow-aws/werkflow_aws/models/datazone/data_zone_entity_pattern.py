from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_zone_filter_clause import DataZoneFilterClause


class DataZoneEntityPattern(BaseModel):
    entityType: Literal['LINEAGE_NODE']
    identifier: StrictStr
    filters: DataZoneFilterClause | None = None
