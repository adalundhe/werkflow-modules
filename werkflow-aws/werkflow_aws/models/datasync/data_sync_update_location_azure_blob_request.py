from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_sync_azure_blob_sas_configuration import DataSyncAzureBlobSasConfiguration
from .data_sync_azure_federated_identity_config import DataSyncAzureFederatedIdentityConfig
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig


class DataSyncUpdateLocationAzureBlobRequest(BaseModel):
    LocationArn: StrictStr
    Subdirectory: StrictStr | None = None
    AuthenticationType: Literal['SAS', 'NONE', 'OIDC'] | None = None
    SasConfiguration: DataSyncAzureBlobSasConfiguration | None = None
    FederatedIdentity: DataSyncAzureFederatedIdentityConfig | None = None
    BlobType: Literal['BLOCK'] | None = None
    AccessTier: Literal['HOT', 'COOL', 'ARCHIVE'] | None = None
    AgentArns: list[StrictStr] | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
