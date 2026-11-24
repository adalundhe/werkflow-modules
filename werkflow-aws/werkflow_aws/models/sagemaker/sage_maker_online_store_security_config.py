from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerOnlineStoreSecurityConfig(BaseModel):
    KmsKeyId: StrictStr | None = None
