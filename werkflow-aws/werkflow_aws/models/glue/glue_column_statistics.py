from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_column_statistics_data import GlueColumnStatisticsData


class GlueColumnStatistics(BaseModel):
    ColumnName: StrictStr | None = None
    ColumnType: StrictStr | None = None
    AnalyzedTime: datetime.datetime | StrictStr | None = None
    StatisticsData: GlueColumnStatisticsData | None = None
