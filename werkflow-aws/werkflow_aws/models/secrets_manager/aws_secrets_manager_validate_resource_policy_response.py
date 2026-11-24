from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool
from .aws_secrets_manager_validation_errors_entry import AWSSecretsManagerValidationErrorsEntry


class AWSSecretsManagerValidateResourcePolicyResponse(BaseModel):
    PolicyValidationPassed: StrictBool | None = None
    ValidationErrors: list[AWSSecretsManagerValidationErrorsEntry] | None = None
    ResponseMetadata: dict[str, Any] | None = None
