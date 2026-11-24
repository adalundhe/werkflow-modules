from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_hdfs_name_node import DataSyncHdfsNameNode
from .data_sync_managed_secret_config import DataSyncManagedSecretConfig
from .data_sync_qop_configuration import DataSyncQopConfiguration


class DataSyncDescribeLocationHdfsResponse(BaseModel):
    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
    NameNodes: list[DataSyncHdfsNameNode] | None = None
    BlockSize: StrictInt | None = None
    ReplicationFactor: StrictInt | None = None
    KmsKeyProviderUri: StrictStr | None = None
    QopConfiguration: DataSyncQopConfiguration | None = None
    AuthenticationType: StrictStr | None = None
    SimpleUser: StrictStr | None = None
    KerberosPrincipal: StrictStr | None = None
    AgentArns: list[StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ManagedSecretConfig: DataSyncManagedSecretConfig | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
