from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr

if TYPE_CHECKING:
    from .timestream_query_datum import TimestreamQueryDatum


class TimestreamQueryTimeSeriesDataPoint(BaseModel):
    Time: StrictStr | None = None
    Value: TimestreamQueryDatum | None = None
