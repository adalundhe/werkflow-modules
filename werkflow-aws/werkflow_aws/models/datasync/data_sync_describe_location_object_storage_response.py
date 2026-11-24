from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_managed_secret_config import DataSyncManagedSecretConfig
from .data_sync_object_storage_federated_identity_config import DataSyncObjectStorageFederatedIdentityConfig


class DataSyncDescribeLocationObjectStorageResponse(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
    AccessKey: StrictStr | None = None
    FederatedIdentity: DataSyncObjectStorageFederatedIdentityConfig | None = None
    ServerPort: StrictInt | None = None
    ServerProtocol: StrictStr | None = None
    AgentArns: list[StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ServerCertificate: StrictBytes | Any | None = None
    ManagedSecretConfig: DataSyncManagedSecretConfig | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
