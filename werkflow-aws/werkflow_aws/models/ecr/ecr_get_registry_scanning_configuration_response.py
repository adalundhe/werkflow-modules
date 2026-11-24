from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_registry_scanning_configuration import ECRRegistryScanningConfiguration


class ECRGetRegistryScanningConfigurationResponse(BaseModel):
    registryId: StrictStr | None = None
    scanningConfiguration: ECRRegistryScanningConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
