from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .config_service_failed_remediation_batch import ConfigServiceFailedRemediationBatch


class ConfigServicePutRemediationConfigurationsResponse(BaseModel):
    FailedBatches: list[ConfigServiceFailedRemediationBatch] | None = None
    ResponseMetadata: dict[str, Any] | None = None
