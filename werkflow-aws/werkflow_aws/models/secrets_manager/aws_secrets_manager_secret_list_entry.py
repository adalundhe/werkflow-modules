from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .aws_secrets_manager_rotation_rules import AWSSecretsManagerRotationRules
from .aws_secrets_manager_tag import AWSSecretsManagerTag


class AWSSecretsManagerSecretListEntry(BaseModel):
    ARN: StrictStr | None = None
    Name: StrictStr | None = None
    Type: StrictStr | None = None
    Description: StrictStr | None = None
    KmsKeyId: StrictStr | None = None
    RotationEnabled: StrictBool | None = None
    RotationLambdaARN: StrictStr | None = None
    RotationRules: AWSSecretsManagerRotationRules | None = None
    LastRotatedDate: datetime.datetime | None = None
    LastChangedDate: datetime.datetime | None = None
    LastAccessedDate: datetime.datetime | None = None
    DeletedDate: datetime.datetime | None = None
    NextRotationDate: datetime.datetime | None = None
    Tags: list[AWSSecretsManagerTag] | None = None
    SecretVersionsToStages: dict[StrictStr, list[StrictStr]] | None = None
    OwningService: StrictStr | None = None
    CreatedDate: datetime.datetime | None = None
    PrimaryRegion: StrictStr | None = None
