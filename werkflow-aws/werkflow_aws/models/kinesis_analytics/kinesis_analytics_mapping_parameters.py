from __future__ import annotations
from pydantic import BaseModel
from .kinesis_analytics_csv_mapping_parameters import KinesisAnalyticsCSVMappingParameters
from .kinesis_analytics_json_mapping_parameters import KinesisAnalyticsJSONMappingParameters


class KinesisAnalyticsMappingParameters(BaseModel):
    JSONMappingParameters: KinesisAnalyticsJSONMappingParameters | None = None
    CSVMappingParameters: KinesisAnalyticsCSVMappingParameters | None = None
