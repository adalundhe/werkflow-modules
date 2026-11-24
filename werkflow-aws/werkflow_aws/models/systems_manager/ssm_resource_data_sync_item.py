from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ssm_resource_data_sync_s3_destination import SSMResourceDataSyncS3Destination
from .ssm_resource_data_sync_source_with_state import SSMResourceDataSyncSourceWithState


class SSMResourceDataSyncItem(BaseModel):
    SyncName: StrictStr | None = None
    SyncType: StrictStr | None = None
    SyncSource: SSMResourceDataSyncSourceWithState | None = None
    S3Destination: SSMResourceDataSyncS3Destination | None = None
    LastSyncTime: datetime.datetime | StrictStr | None = None
    LastSuccessfulSyncTime: datetime.datetime | StrictStr | None = None
    SyncLastModifiedTime: datetime.datetime | StrictStr | None = None
    LastStatus: StrictStr | None = None
    SyncCreatedTime: datetime.datetime | StrictStr | None = None
    LastSyncStatusMessage: StrictStr | None = None
