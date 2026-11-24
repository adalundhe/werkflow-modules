from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_s3_reference_data_source_update import KinesisAnalyticsS3ReferenceDataSourceUpdate
from .kinesis_analytics_source_schema import KinesisAnalyticsSourceSchema


class KinesisAnalyticsReferenceDataSourceUpdate(BaseModel):
    ReferenceId: StrictStr
    TableNameUpdate: StrictStr | None = None
    S3ReferenceDataSourceUpdate: KinesisAnalyticsS3ReferenceDataSourceUpdate | None = None
    ReferenceSchemaUpdate: KinesisAnalyticsSourceSchema | None = None
