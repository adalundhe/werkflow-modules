from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .kinesis_analytics_application_operation_description import KinesisAnalyticsApplicationOperationDescription
from .kinesis_analytics_encryption_configuration_description import KinesisAnalyticsEncryptionConfigurationDescription
from .kinesis_analytics_snapshot_operation_failure_details import KinesisAnalyticsSnapshotOperationFailureDetails
from .kinesis_analytics_snapshot_operation_location_description import KinesisAnalyticsSnapshotOperationLocationDescription


class KinesisAnalyticsSnapshotOperationInfoDetails(BaseModel):
    SnapshotOperationId: StrictStr | None = None
    SnapshotOperation: StrictStr | None = None
    SnapshotOperationStatus: StrictStr | None = None
    SnapshotArn: StrictStr | None = None
    SourceEncryptionConfigurationDescription: KinesisAnalyticsEncryptionConfigurationDescription | None = None
    DestinationEncryptionConfigurationDescription: KinesisAnalyticsEncryptionConfigurationDescription | None = None
    SnapshotSourceLocationDescription: KinesisAnalyticsSnapshotOperationLocationDescription | None = None
    SnapshotDestinationLocationDescription: KinesisAnalyticsSnapshotOperationLocationDescription | None = None
    ApplicationOperationDescription: KinesisAnalyticsApplicationOperationDescription | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    EndTime: datetime.datetime | StrictStr | None = None
    SnapshotOperationFailureDetails: KinesisAnalyticsSnapshotOperationFailureDetails | None = None
