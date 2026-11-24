from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_hdfs_name_node import DataSyncHdfsNameNode
from .data_sync_qop_configuration import DataSyncQopConfiguration


class DataSyncUpdateLocationHdfsRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    LocationArn: StrictStr
    Subdirectory: StrictStr | None = None
    NameNodes: list[DataSyncHdfsNameNode] | None = None
    BlockSize: StrictInt | None = None
    ReplicationFactor: StrictInt | None = None
    KmsKeyProviderUri: StrictStr | None = None
    QopConfiguration: DataSyncQopConfiguration | None = None
    AuthenticationType: Literal['SIMPLE', 'KERBEROS'] | None = None
    SimpleUser: StrictStr | None = None
    KerberosPrincipal: StrictStr | None = None
    KerberosKeytab: StrictBytes | BinaryIO | StrictStr | None = None
    KerberosKrb5Conf: StrictBytes | BinaryIO | StrictStr | None = None
    AgentArns: list[StrictStr] | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
