from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .aws_secrets_manager_rotation_rules import AWSSecretsManagerRotationRules


class AWSSecretsManagerRotateSecretRequest(BaseModel):
    SecretId: StrictStr
    ClientRequestToken: StrictStr | None = None
    RotationLambdaARN: StrictStr | None = None
    RotationRules: AWSSecretsManagerRotationRules | None = None
    RotateImmediately: StrictBool | None = None
