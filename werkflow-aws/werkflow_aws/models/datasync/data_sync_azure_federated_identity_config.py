from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .data_sync_azure_oidc_config import DataSyncAzureOidcConfig


class DataSyncAzureFederatedIdentityConfig(BaseModel):
    AwsIamRole: StrictStr | None = None
    AzureOidc: DataSyncAzureOidcConfig | None = None
