from __future__ import annotations
from pydantic import BaseModel
from .data_sync_fsx_protocol_nfs import DataSyncFsxProtocolNfs
from .data_sync_fsx_update_protocol_smb import DataSyncFsxUpdateProtocolSmb


class DataSyncFsxUpdateProtocol(BaseModel):
    NFS: DataSyncFsxProtocolNfs | None = None
    SMB: DataSyncFsxUpdateProtocolSmb | None = None
