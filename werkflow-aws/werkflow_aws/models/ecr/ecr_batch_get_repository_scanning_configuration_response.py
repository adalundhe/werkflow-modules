from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_repository_scanning_configuration import ECRRepositoryScanningConfiguration
from .ecr_repository_scanning_configuration_failure import ECRRepositoryScanningConfigurationFailure


class ECRBatchGetRepositoryScanningConfigurationResponse(BaseModel):
    scanningConfigurations: list[ECRRepositoryScanningConfiguration] | None = None
    failures: list[ECRRepositoryScanningConfigurationFailure] | None = None
    ResponseMetadata: dict[str, Any] | None = None
