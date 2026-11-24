from __future__ import annotations
from pydantic import BaseModel
from .kinesis_analytics_input_update import KinesisAnalyticsInputUpdate
from .kinesis_analytics_output_update import KinesisAnalyticsOutputUpdate
from .kinesis_analytics_reference_data_source_update import KinesisAnalyticsReferenceDataSourceUpdate


class KinesisAnalyticsSqlApplicationConfigurationUpdate(BaseModel):
    InputUpdates: list[KinesisAnalyticsInputUpdate] | None = None
    OutputUpdates: list[KinesisAnalyticsOutputUpdate] | None = None
    ReferenceDataSourceUpdates: list[KinesisAnalyticsReferenceDataSourceUpdate] | None = None
