from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .bedrock_trusted_access_program_application_result import BedrockTrustedAccessProgramApplicationResult


class BedrockStartTrustedAccessProgramOrganizationApplicationResponse(BaseModel):
    result: BedrockTrustedAccessProgramApplicationResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
