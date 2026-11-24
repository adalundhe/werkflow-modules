from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCommitUpdateRepositoryEncryptionKeyResponse(BaseModel):
    repositoryId: StrictStr | None = None
    kmsKeyId: StrictStr | None = None
    originalKmsKeyId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
