from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_s3_prefix_location import KinesisAnalyticsS3PrefixLocation
from .kinesis_analytics_snapshot_encryption_configuration import KinesisAnalyticsSnapshotEncryptionConfiguration


class KinesisAnalyticsExportDestinationConfiguration(BaseModel):
    DestinationType: Literal['S3']
    ExportRoleArn: StrictStr
    DestinationS3PrefixLocation: KinesisAnalyticsS3PrefixLocation
    DestinationEncryptionConfiguration: KinesisAnalyticsSnapshotEncryptionConfiguration | None = None
