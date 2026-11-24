from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelCardSecurityConfig(BaseModel):
    KmsKeyId: StrictStr | None = None
