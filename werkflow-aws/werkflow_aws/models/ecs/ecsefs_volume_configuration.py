from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .ecsefs_authorization_config import ECSEFSAuthorizationConfig


class ECSEFSVolumeConfiguration(BaseModel):
    fileSystemId: StrictStr | None = None
    rootDirectory: StrictStr | None = None
    transitEncryption: StrictStr | None = None
    transitEncryptionPort: StrictInt | None = None
    authorizationConfig: ECSEFSAuthorizationConfig | None = None
