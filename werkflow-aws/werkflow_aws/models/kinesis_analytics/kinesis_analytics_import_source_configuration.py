from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_s3_prefix_location import KinesisAnalyticsS3PrefixLocation
from .kinesis_analytics_snapshot_encryption_configuration import KinesisAnalyticsSnapshotEncryptionConfiguration


class KinesisAnalyticsImportSourceConfiguration(BaseModel):
    SourceType: Literal['S3']
    ImportRoleArn: StrictStr
    SourceS3PrefixLocation: KinesisAnalyticsS3PrefixLocation
    SourceEncryptionConfiguration: KinesisAnalyticsSnapshotEncryptionConfiguration | None = None
