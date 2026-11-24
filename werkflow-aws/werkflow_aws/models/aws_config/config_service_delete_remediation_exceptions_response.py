from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_failed_delete_remediation_exceptions_batch import ConfigServiceFailedDeleteRemediationExceptionsBatch


class ConfigServiceDeleteRemediationExceptionsResponse(BaseModel):
    FailedBatches: list[ConfigServiceFailedDeleteRemediationExceptionsBatch] | None = None
    ResponseMetadata: dict[str, Any] | None = None
