from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class AWSSecretsManagerListSecretVersionIdsRequest(BaseModel):
    SecretId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
    IncludeDeprecated: StrictBool | None = None
