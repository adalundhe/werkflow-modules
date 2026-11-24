from __future__ import annotations
from pydantic import BaseModel
from .data_sync_nfs_mount_options import DataSyncNfsMountOptions


class DataSyncFsxProtocolNfs(BaseModel):
    MountOptions: DataSyncNfsMountOptions | None = None
