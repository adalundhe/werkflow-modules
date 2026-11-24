from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr

if TYPE_CHECKING:
    from .timestream_query_column_info import TimestreamQueryColumnInfo


class TimestreamQueryType(BaseModel):
    ScalarType: StrictStr | None = None
    ArrayColumnInfo: TimestreamQueryColumnInfo | None = None
    TimeSeriesMeasureValueColumnInfo: TimestreamQueryColumnInfo | None = None
    RowColumnInfo: list[TimestreamQueryColumnInfo] | None = None
