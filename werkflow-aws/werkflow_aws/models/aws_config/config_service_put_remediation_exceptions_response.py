from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_failed_remediation_exception_batch import ConfigServiceFailedRemediationExceptionBatch


class ConfigServicePutRemediationExceptionsResponse(BaseModel):
    FailedBatches: list[ConfigServiceFailedRemediationExceptionBatch] | None = None
    ResponseMetadata: dict[str, Any] | None = None
