from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeCommitUpdateRepositoryEncryptionKeyRequest(BaseModel):
    repositoryName: StrictStr
    kmsKeyId: StrictStr
