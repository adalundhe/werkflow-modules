from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_record_column import KinesisAnalyticsRecordColumn
from .kinesis_analytics_record_format import KinesisAnalyticsRecordFormat


class KinesisAnalyticsSourceSchema(BaseModel):
    RecordFormat: KinesisAnalyticsRecordFormat | None = None
    RecordEncoding: StrictStr | None = None
    RecordColumns: list[KinesisAnalyticsRecordColumn] | None = None
