from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_snapshot_encryption_configuration import KinesisAnalyticsSnapshotEncryptionConfiguration
from .kinesis_analytics_snapshot_source_description import KinesisAnalyticsSnapshotSourceDescription


class KinesisAnalyticsSnapshotInfoDetails(BaseModel):
    SnapshotName: StrictStr | None = None
    SnapshotArn: StrictStr | None = None
    SnapshotDescription: StrictStr | None = None
    SnapshotStatus: StrictStr | None = None
    SnapshotCreationTimestamp: datetime.datetime | StrictStr | None = None
    RuntimeEnvironment: StrictStr | None = None
    SnapshotSizeInBytes: StrictInt | None = None
    SnapshotEncryptionConfigurationDescription: KinesisAnalyticsSnapshotEncryptionConfiguration | None = None
    SnapshotInitiator: StrictStr | None = None
    SnapshotInitiatorOperation: StrictStr | None = None
    SnapshotSourceDescription: KinesisAnalyticsSnapshotSourceDescription | None = None
    SnapshotFormat: StrictStr | None = None
