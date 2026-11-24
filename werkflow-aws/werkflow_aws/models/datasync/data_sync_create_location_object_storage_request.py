from __future__ import annotations
from typing import BinaryIO, Literal
from pydantic import BaseModel, ConfigDict, StrictBytes, StrictInt, StrictStr
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_object_storage_federated_identity_config import DataSyncObjectStorageFederatedIdentityConfig
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncCreateLocationObjectStorageRequest(BaseModel):
    model_config = ConfigDict(arbitrary_types_allowed=True)

    ServerHostname: StrictStr
    BucketName: StrictStr
    ServerPort: StrictInt | None = None
    ServerProtocol: Literal['HTTPS', 'HTTP'] | None = None
    Subdirectory: StrictStr | None = None
    AccessKey: StrictStr | None = None
    SecretKey: StrictStr | None = None
    FederatedIdentity: DataSyncObjectStorageFederatedIdentityConfig | None = None
    AgentArns: list[StrictStr] | None = None
    Tags: list[DataSyncTagListEntry] | None = None
    ServerCertificate: StrictBytes | BinaryIO | StrictStr | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
