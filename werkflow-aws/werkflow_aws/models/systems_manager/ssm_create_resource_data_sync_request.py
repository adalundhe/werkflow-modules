from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_resource_data_sync_s3_destination import SSMResourceDataSyncS3Destination
from .ssm_resource_data_sync_source import SSMResourceDataSyncSource


class SSMCreateResourceDataSyncRequest(BaseModel):
    SyncName: StrictStr
    S3Destination: SSMResourceDataSyncS3Destination | None = None
    SyncType: StrictStr | None = None
    SyncSource: SSMResourceDataSyncSource | None = None
