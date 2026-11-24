from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_zone_filter_expression import DataZoneFilterExpression


class DataZoneRelationalFilterConfiguration(BaseModel):
    databaseName: StrictStr | None = None
    schemaName: StrictStr | None = None
    filterExpressions: list[DataZoneFilterExpression] | None = None
