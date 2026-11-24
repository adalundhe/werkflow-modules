from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AWSSecretsManagerListResourcePoliciesRequest(BaseModel):
    SecretId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
