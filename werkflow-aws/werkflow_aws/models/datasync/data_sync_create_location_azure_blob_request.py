from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .data_sync_azure_blob_sas_configuration import DataSyncAzureBlobSasConfiguration
from .data_sync_azure_federated_identity_config import DataSyncAzureFederatedIdentityConfig
from .data_sync_cmk_secret_config import DataSyncCmkSecretConfig
from .data_sync_custom_secret_config import DataSyncCustomSecretConfig
from .data_sync_tag_list_entry import DataSyncTagListEntry


class DataSyncCreateLocationAzureBlobRequest(BaseModel):
    ContainerUrl: StrictStr
    AuthenticationType: Literal['SAS', 'NONE', 'OIDC']
    SasConfiguration: DataSyncAzureBlobSasConfiguration | None = None
    FederatedIdentity: DataSyncAzureFederatedIdentityConfig | None = None
    BlobType: Literal['BLOCK'] | None = None
    AccessTier: Literal['HOT', 'COOL', 'ARCHIVE'] | None = None
    Subdirectory: StrictStr | None = None
    AgentArns: list[StrictStr] | None = None
    Tags: list[DataSyncTagListEntry] | None = None
    CmkSecretConfig: DataSyncCmkSecretConfig | None = None
    CustomSecretConfig: DataSyncCustomSecretConfig | None = None
