from __future__ import annotations
from pydantic import BaseModel
from .ecr_signing_configuration import ECRSigningConfiguration


class ECRPutSigningConfigurationRequest(BaseModel):
    signingConfiguration: ECRSigningConfiguration
