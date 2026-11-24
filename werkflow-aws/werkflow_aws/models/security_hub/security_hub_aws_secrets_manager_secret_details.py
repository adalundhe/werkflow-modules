from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_hub_aws_secrets_manager_secret_rotation_rules import SecurityHubAwsSecretsManagerSecretRotationRules


class SecurityHubAwsSecretsManagerSecretDetails(BaseModel):
    RotationRules: SecurityHubAwsSecretsManagerSecretRotationRules | None = None
    RotationOccurredWithinFrequency: StrictBool | None = None
    KmsKeyId: StrictStr | None = None
    RotationEnabled: StrictBool | None = None
    RotationLambdaArn: StrictStr | None = None
    Deleted: StrictBool | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
