from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerEncryptionConfiguration(BaseModel):
    KmsKey: StrictStr | None = None
