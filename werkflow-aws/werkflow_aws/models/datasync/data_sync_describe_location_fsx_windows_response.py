from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_managed_secret_config import DataSyncManagedSecretConfig


class DataSyncDescribeLocationFsxWindowsResponse(BaseModel):
    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
    SecurityGroupArns: list[StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    User: StrictStr | None = None
    Domain: StrictStr | None = None
    ManagedSecretConfig: DataSyncManagedSecretConfig | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
