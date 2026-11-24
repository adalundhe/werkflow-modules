from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .batch_efs_authorization_config import BatchEFSAuthorizationConfig


class BatchEFSVolumeConfiguration(BaseModel):
    fileSystemId: StrictStr | None = None
    rootDirectory: StrictStr | None = None
    transitEncryption: StrictStr | None = None
    transitEncryptionPort: StrictInt | None = None
    authorizationConfig: BatchEFSAuthorizationConfig | None = None
