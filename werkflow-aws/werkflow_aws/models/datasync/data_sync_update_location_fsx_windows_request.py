from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig


class DataSyncUpdateLocationFsxWindowsRequest(BaseModel):
    LocationArn: StrictStr
    Subdirectory: StrictStr | None = None
    Domain: StrictStr | None = None
    User: StrictStr | None = None
    Password: StrictStr | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
