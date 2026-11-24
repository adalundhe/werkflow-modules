from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ecr_signing_configuration import ECRSigningConfiguration


class ECRGetSigningConfigurationResponse(BaseModel):
    registryId: StrictStr | None = None
    signingConfiguration: ECRSigningConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
