from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_record_column import KinesisAnalyticsRecordColumn
from .kinesis_analytics_record_format import KinesisAnalyticsRecordFormat


class KinesisAnalyticsInputSchemaUpdate(BaseModel):
    RecordFormatUpdate: KinesisAnalyticsRecordFormat | None = None
    RecordEncodingUpdate: StrictStr | None = None
    RecordColumnUpdates: list[KinesisAnalyticsRecordColumn] | None = None
