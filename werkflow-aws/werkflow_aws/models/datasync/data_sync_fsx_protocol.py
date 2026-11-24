from __future__ import annotations
from pydantic import BaseModel
from .data_sync_fsx_protocol_nfs import DataSyncFsxProtocolNfs
from .data_sync_fsx_protocol_smb import DataSyncFsxProtocolSmb


class DataSyncFsxProtocol(BaseModel):
    NFS: DataSyncFsxProtocolNfs | None = None
    SMB: DataSyncFsxProtocolSmb | None = None
