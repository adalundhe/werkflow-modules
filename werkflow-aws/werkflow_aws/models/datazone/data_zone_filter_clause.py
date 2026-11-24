from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .data_zone_filter import DataZoneFilter


class DataZoneFilterClause(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    filter: DataZoneFilter | None = None
    and_: list[DataZoneFilterClause] | None = Field(default=None, alias='and')
    or_: list[DataZoneFilterClause] | None = Field(default=None, alias='or')
