from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_hdfs_name_node import DataSyncHdfsNameNode
from .data_sync_qop_configuration import DataSyncQopConfiguration
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncCreateLocationHdfsRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    NameNodes: list[DataSyncHdfsNameNode]
    AuthenticationType: Literal['SIMPLE', 'KERBEROS']
    AgentArns: list[StrictStr]
    Subdirectory: StrictStr | None = None
    BlockSize: StrictInt | None = None
    ReplicationFactor: StrictInt | None = None
    KmsKeyProviderUri: StrictStr | None = None
    QopConfiguration: DataSyncQopConfiguration | None = None
    SimpleUser: StrictStr | None = None
    KerberosPrincipal: StrictStr | None = None
    KerberosKeytab: StrictBytes | BinaryIO | StrictStr | None = None
    KerberosKrb5Conf: StrictBytes | BinaryIO | StrictStr | None = None
    Tags: list[DataSyncTagListEntry] | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
