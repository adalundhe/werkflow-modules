from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_column_statistics import GlueColumnStatistics


class GlueUpdateColumnStatisticsForTableRequest(BaseModel):
    DatabaseName: StrictStr
    TableName: StrictStr
    ColumnStatisticsList: list[GlueColumnStatistics]
    CatalogId: StrictStr | None = None
