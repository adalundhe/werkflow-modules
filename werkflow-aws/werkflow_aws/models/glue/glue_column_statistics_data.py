from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_binary_column_statistics_data import GlueBinaryColumnStatisticsData
from .glue_boolean_column_statistics_data import GlueBooleanColumnStatisticsData
from .glue_date_column_statistics_data import GlueDateColumnStatisticsData
from .glue_decimal_column_statistics_data import GlueDecimalColumnStatisticsData
from .glue_double_column_statistics_data import GlueDoubleColumnStatisticsData
from .glue_long_column_statistics_data import GlueLongColumnStatisticsData
from .glue_string_column_statistics_data import GlueStringColumnStatisticsData


class GlueColumnStatisticsData(BaseModel):
    Type: StrictStr | None = None
    BooleanColumnStatisticsData: GlueBooleanColumnStatisticsData | None = None
    DateColumnStatisticsData: GlueDateColumnStatisticsData | None = None
    DecimalColumnStatisticsData: GlueDecimalColumnStatisticsData | None = None
    DoubleColumnStatisticsData: GlueDoubleColumnStatisticsData | None = None
    LongColumnStatisticsData: GlueLongColumnStatisticsData | None = None
    StringColumnStatisticsData: GlueStringColumnStatisticsData | None = None
    BinaryColumnStatisticsData: GlueBinaryColumnStatisticsData | None = None
