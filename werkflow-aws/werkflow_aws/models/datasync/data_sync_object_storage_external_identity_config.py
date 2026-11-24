from __future__ import annotations
from pydantic import BaseModel
from .data_sync_google_oidc_config import DataSyncGoogleOidcConfig


class DataSyncObjectStorageExternalIdentityConfig(BaseModel):
    GoogleOidc: DataSyncGoogleOidcConfig | None = None
