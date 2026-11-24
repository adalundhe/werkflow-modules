from __future__ import annotations
from pydantic import BaseModel
from .kinesis_analytics_input import KinesisAnalyticsInput
from .kinesis_analytics_output import KinesisAnalyticsOutput
from .kinesis_analytics_reference_data_source import KinesisAnalyticsReferenceDataSource


class KinesisAnalyticsSqlApplicationConfiguration(BaseModel):
    Inputs: list[KinesisAnalyticsInput] | None = None
    Outputs: list[KinesisAnalyticsOutput] | None = None
    ReferenceDataSources: list[KinesisAnalyticsReferenceDataSource] | None = None
