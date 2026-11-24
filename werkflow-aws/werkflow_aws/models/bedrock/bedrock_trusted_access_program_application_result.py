from __future__ import annotations
from pydantic import BaseModel
from .bedrock_trusted_access_program_provider_handoff import BedrockTrustedAccessProgramProviderHandoff


class BedrockTrustedAccessProgramApplicationResult(BaseModel):
    providerHandoff: BedrockTrustedAccessProgramProviderHandoff | None = None
