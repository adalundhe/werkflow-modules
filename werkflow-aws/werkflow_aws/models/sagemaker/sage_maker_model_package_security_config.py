from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SageMakerModelPackageSecurityConfig(BaseModel):
    KmsKeyId: StrictStr | None = None
