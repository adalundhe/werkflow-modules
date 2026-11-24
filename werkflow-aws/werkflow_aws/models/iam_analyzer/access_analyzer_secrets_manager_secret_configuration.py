from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerSecretsManagerSecretConfiguration(BaseModel):
    kmsKeyId: StrictStr | None = None
    secretPolicy: StrictStr | None = None
