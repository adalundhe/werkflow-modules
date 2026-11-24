from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SecurityHubAwsSecretsManagerSecretRotationRules(BaseModel):
    AutomaticallyAfterDays: StrictInt | None = None
