from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .aws_secrets_manager_api_error_type import AWSSecretsManagerAPIErrorType
from .aws_secrets_manager_secret_value_entry import AWSSecretsManagerSecretValueEntry


class AWSSecretsManagerBatchGetSecretValueResponse(BaseModel):
    SecretValues: list[AWSSecretsManagerSecretValueEntry] | None = None
    NextToken: StrictStr | None = None
    Errors: list[AWSSecretsManagerAPIErrorType] | None = None
    ResponseMetadata: dict[str, Any] | None = None
