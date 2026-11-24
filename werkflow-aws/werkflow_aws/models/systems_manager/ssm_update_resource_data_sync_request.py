from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .ssm_resource_data_sync_source import SSMResourceDataSyncSource


class SSMUpdateResourceDataSyncRequest(BaseModel):
    SyncName: StrictStr
    SyncType: StrictStr
    SyncSource: SSMResourceDataSyncSource
