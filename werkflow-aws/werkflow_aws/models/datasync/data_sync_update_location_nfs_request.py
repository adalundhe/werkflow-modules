from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_nfs_mount_options import DataSyncNfsMountOptions
from .data_sync_on_prem_config import DataSyncOnPremConfig


class DataSyncUpdateLocationNfsRequest(BaseModel):
    LocationArn: StrictStr
    Subdirectory: StrictStr | None = None
    ServerHostname: StrictStr | None = None
    OnPremConfig: DataSyncOnPremConfig | None = None
    MountOptions: DataSyncNfsMountOptions | None = None
