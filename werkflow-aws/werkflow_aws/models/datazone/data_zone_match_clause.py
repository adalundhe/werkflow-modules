from __future__ import annotations
from pydantic import BaseModel
from .data_zone_entity_pattern import DataZoneEntityPattern
from .data_zone_relation_pattern import DataZoneRelationPattern


class DataZoneMatchClause(BaseModel):
    relationPattern: DataZoneRelationPattern | None = None
    entityPattern: DataZoneEntityPattern | None = None
