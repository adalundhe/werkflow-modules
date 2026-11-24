from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .timestream_query_row import TimestreamQueryRow
from .timestream_query_time_series_data_point import TimestreamQueryTimeSeriesDataPoint


class TimestreamQueryDatum(BaseModel):
    ScalarValue: StrictStr | None = None
    TimeSeriesValue: list[TimestreamQueryTimeSeriesDataPoint] | None = None
    ArrayValue: list[TimestreamQueryDatum] | None = None
    RowValue: TimestreamQueryRow | None = None
    NullValue: StrictBool | None = None
