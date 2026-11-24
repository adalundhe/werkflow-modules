from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .aws_secrets_manager_tag import AWSSecretsManagerTag


class AWSSecretsManagerTagResourceRequest(BaseModel):
    SecretId: StrictStr
    Tags: list[AWSSecretsManagerTag]
