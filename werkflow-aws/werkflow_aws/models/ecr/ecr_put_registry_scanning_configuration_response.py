from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_registry_scanning_configuration import ECRRegistryScanningConfiguration


class ECRPutRegistryScanningConfigurationResponse(BaseModel):
    registryScanningConfiguration: ECRRegistryScanningConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
