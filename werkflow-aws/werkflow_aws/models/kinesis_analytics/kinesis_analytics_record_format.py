from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_mapping_parameters import KinesisAnalyticsMappingParameters


class KinesisAnalyticsRecordFormat(BaseModel):
    RecordFormatType: StrictStr | None = None
    MappingParameters: KinesisAnalyticsMappingParameters | None = None
