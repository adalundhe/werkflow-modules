from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_s3_reference_data_source import KinesisAnalyticsS3ReferenceDataSource
from .kinesis_analytics_source_schema import KinesisAnalyticsSourceSchema


class KinesisAnalyticsReferenceDataSource(BaseModel):
    TableName: StrictStr
    ReferenceSchema: KinesisAnalyticsSourceSchema
    S3ReferenceDataSource: KinesisAnalyticsS3ReferenceDataSource | None = None
