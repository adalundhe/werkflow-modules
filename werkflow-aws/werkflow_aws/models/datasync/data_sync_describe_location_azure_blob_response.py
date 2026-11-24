from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .data_sync_azure_federated_identity_config import DataSyncAzureFederatedIdentityConfig
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_managed_secret_config import DataSyncManagedSecretConfig


class DataSyncDescribeLocationAzureBlobResponse(BaseModel):
    LocationArn: StrictStr | None = None
    LocationUri: StrictStr | None = None
    AuthenticationType: StrictStr | None = None
    FederatedIdentity: DataSyncAzureFederatedIdentityConfig | None = None
    BlobType: StrictStr | None = None
    AccessTier: StrictStr | None = None
    AgentArns: list[StrictStr] | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ManagedSecretConfig: DataSyncManagedSecretConfig | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
    ResponseMetadata: dict[str, Any] | None = None
