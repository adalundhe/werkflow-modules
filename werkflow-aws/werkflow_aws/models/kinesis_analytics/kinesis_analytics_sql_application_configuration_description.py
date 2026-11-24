from __future__ import annotations
from pydantic import BaseModel
from .kinesis_analytics_input_description import KinesisAnalyticsInputDescription
from .kinesis_analytics_output_description import KinesisAnalyticsOutputDescription
from .kinesis_analytics_reference_data_source_description import KinesisAnalyticsReferenceDataSourceDescription


class KinesisAnalyticsSqlApplicationConfigurationDescription(BaseModel):
    InputDescriptions: list[KinesisAnalyticsInputDescription] | None = None
    OutputDescriptions: list[KinesisAnalyticsOutputDescription] | None = None
    ReferenceDataSourceDescriptions: list[KinesisAnalyticsReferenceDataSourceDescription] | None = None
