from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_smb_mount_options import DataSyncSmbMountOptions
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncCreateLocationSmbRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    Subdirectory: StrictStr
    ServerHostname: StrictStr
    AgentArns: list[StrictStr]
    User: StrictStr | None = None
    Domain: StrictStr | None = None
    Password: StrictStr | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
    MountOptions: DataSyncSmbMountOptions | None = None
    Tags: list[DataSyncTagListEntry] | None = None
    AuthenticationType: Literal['NTLM', 'KERBEROS'] | None = None
    DnsIpAddresses: list[StrictStr] | None = None
    KerberosPrincipal: StrictStr | None = None
    KerberosKeytab: StrictBytes | BinaryIO | StrictStr | None = None
    KerberosKrb5Conf: StrictBytes | BinaryIO | StrictStr | None = None
