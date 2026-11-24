from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_managed_secret_config import DataSyncManagedSecretConfig
from .data_sync_smb_mount_options import DataSyncSmbMountOptions


class DataSyncDescribeLocationSmbResponse(BaseModel):
    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
    AgentArns: list[StrictStr] | None = None
    User: StrictStr | None = None
    Domain: StrictStr | None = None
    MountOptions: DataSyncSmbMountOptions | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    DnsIpAddresses: list[StrictStr] | None = None
    KerberosPrincipal: StrictStr | None = None
    AuthenticationType: StrictStr | None = None
    ManagedSecretConfig: DataSyncManagedSecretConfig | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
