from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_smb_mount_options import DataSyncSmbMountOptions


class DataSyncUpdateLocationSmbRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    LocationArn: StrictStr
    Subdirectory: StrictStr | None = None
    ServerHostname: StrictStr | None = None
    User: StrictStr | None = None
    Domain: StrictStr | None = None
    Password: StrictStr | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
    AgentArns: list[StrictStr] | None = None
    MountOptions: DataSyncSmbMountOptions | None = None
    AuthenticationType: Literal['NTLM', 'KERBEROS'] | None = None
    DnsIpAddresses: list[StrictStr] | None = None
    KerberosPrincipal: StrictStr | None = None
    KerberosKeytab: StrictBytes | BinaryIO | StrictStr | None = None
    KerberosKrb5Conf: StrictBytes | BinaryIO | StrictStr | None = None
