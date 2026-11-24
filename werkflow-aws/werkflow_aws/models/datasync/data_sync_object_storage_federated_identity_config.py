from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_object_storage_external_identity_config import DataSyncObjectStorageExternalIdentityConfig


class DataSyncObjectStorageFederatedIdentityConfig(BaseModel):
    AwsIamRole: StrictStr | None = None
    ExternalIdentity: DataSyncObjectStorageExternalIdentityConfig | None = None
