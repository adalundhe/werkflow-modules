from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncCreateLocationFsxWindowsRequest(BaseModel):
    FsxFilesystemArn: StrictStr
    SecurityGroupArns: list[StrictStr]
    User: StrictStr
    Subdirectory: StrictStr | None = None
    Tags: list[DataSyncTagListEntry] | None = None
    Domain: StrictStr | None = None
    Password: StrictStr | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
