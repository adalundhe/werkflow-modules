from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .kinesis_analytics_application_encryption_configuration_description import KinesisAnalyticsApplicationEncryptionConfigurationDescription


class KinesisAnalyticsSnapshotDetails(BaseModel):
    SnapshotName: StrictStr | None = None
    SnapshotStatus: StrictStr | None = None
    ApplicationVersionId: StrictInt | None = None
    SnapshotCreationTimestamp: datetime.datetime | StrictStr | None = None
    RuntimeEnvironment: StrictStr | None = None
    ApplicationEncryptionConfigurationDescription: KinesisAnalyticsApplicationEncryptionConfigurationDescription | None = None
