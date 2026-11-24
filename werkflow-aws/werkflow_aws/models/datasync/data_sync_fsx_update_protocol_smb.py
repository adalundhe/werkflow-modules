from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_smb_mount_options import DataSyncSmbMountOptions


class DataSyncFsxUpdateProtocolSmb(BaseModel):
    Domain: StrictStr | None = None
    MountOptions: DataSyncSmbMountOptions | None = None
    Password: StrictStr | None = None
    User: StrictStr | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
