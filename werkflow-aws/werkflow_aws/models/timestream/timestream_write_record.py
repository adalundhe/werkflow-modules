from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .timestream_write_dimension import TimestreamWriteDimension
from .timestream_write_measure_value import TimestreamWriteMeasureValue


class TimestreamWriteRecord(BaseModel):
    Dimensions: list[TimestreamWriteDimension] | None = None
    MeasureName: StrictStr | None = None
    MeasureValue: StrictStr | None = None
    MeasureValueType: Literal['DOUBLE', 'BIGINT', 'VARCHAR', 'BOOLEAN', 'TIMESTAMP', 'MULTI'] | None = None
    Time: StrictStr | None = None
    TimeUnit: Literal['MILLISECONDS', 'SECONDS', 'MICROSECONDS', 'NANOSECONDS'] | None = None
    Version: StrictInt | None = None
    MeasureValues: list[TimestreamWriteMeasureValue] | None = None
