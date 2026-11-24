from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AWSSecretsManagerUntagResourceRequest(BaseModel):
    SecretId: StrictStr
    TagKeys: list[StrictStr]
