from __future__ import annotations
from pydantic import BaseModel
from .kinesis_analytics_s3_prefix_location import KinesisAnalyticsS3PrefixLocation
from .kinesis_analytics_source_application_description import KinesisAnalyticsSourceApplicationDescription


class KinesisAnalyticsSnapshotSourceDescription(BaseModel):
    S3PrefixLocation: KinesisAnalyticsS3PrefixLocation | None = None
    SourceApplicationDescription: KinesisAnalyticsSourceApplicationDescription | None = None
