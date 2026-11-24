from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerValidateResourcePolicyRequest(BaseModel):
    ResourcePolicy: StrictStr
    SecretId: StrictStr | None = None
