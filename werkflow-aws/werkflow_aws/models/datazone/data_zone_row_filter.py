from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field
from .data_zone_row_filter_expression import DataZoneRowFilterExpression


class DataZoneRowFilter(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    expression: DataZoneRowFilterExpression | None = None
    and_: list[DataZoneRowFilter] | None = Field(default=None, alias='and')
    or_: list[DataZoneRowFilter] | None = Field(default=None, alias='or')
