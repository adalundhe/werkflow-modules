from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AWSSecretsManagerPutResourcePolicyRequest(BaseModel):
    SecretId: StrictStr
    ResourcePolicy: StrictStr
    PolicyName: StrictStr | None = None
    BlockPublicPolicy: StrictBool | None = None
