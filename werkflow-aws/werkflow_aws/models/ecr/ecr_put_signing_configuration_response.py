from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .ecr_signing_configuration import ECRSigningConfiguration


class ECRPutSigningConfigurationResponse(BaseModel):
    signingConfiguration: ECRSigningConfiguration | None = None
    ResponseMetadata: dict[str, Any] | None = None
