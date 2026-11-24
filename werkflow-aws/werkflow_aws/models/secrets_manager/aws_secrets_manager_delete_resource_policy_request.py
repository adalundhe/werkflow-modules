from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerDeleteResourcePolicyRequest(BaseModel):
    SecretId: StrictStr
    PolicyName: StrictStr | None = None
