from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_import_source_configuration import KinesisAnalyticsImportSourceConfiguration
from .kinesis_analytics_snapshot_encryption_configuration import KinesisAnalyticsSnapshotEncryptionConfiguration
from .kinesis_analytics_tag import KinesisAnalyticsTag


class KinesisAnalyticsImportSnapshotRequest(BaseModel):
    SnapshotName: StrictStr
    ImportSourceConfiguration: KinesisAnalyticsImportSourceConfiguration
    DestinationEncryptionConfiguration: KinesisAnalyticsSnapshotEncryptionConfiguration | None = None
    SnapshotDescription: StrictStr | None = None
    SnapshotFormat: Literal['CANONICAL'] | None = None
    Tags: list[KinesisAnalyticsTag] | None = None
