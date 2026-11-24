from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_nfs_mount_options import DataSyncNfsMountOptions
from .data_sync_on_prem_config import DataSyncOnPremConfig
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncCreateLocationNfsRequest(BaseModel):
    Subdirectory: StrictStr
    ServerHostname: StrictStr
    OnPremConfig: DataSyncOnPremConfig
    MountOptions: DataSyncNfsMountOptions | None = None
    Tags: list[DataSyncTagListEntry] | None = None
