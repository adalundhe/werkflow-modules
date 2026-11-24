from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_s3_reference_data_source_description import KinesisAnalyticsS3ReferenceDataSourceDescription
from .kinesis_analytics_source_schema import KinesisAnalyticsSourceSchema


class KinesisAnalyticsReferenceDataSourceDescription(BaseModel):
    ReferenceId: StrictStr | None = None
    TableName: StrictStr | None = None
    S3ReferenceDataSourceDescription: KinesisAnalyticsS3ReferenceDataSourceDescription | None = None
    ReferenceSchema: KinesisAnalyticsSourceSchema | None = None
