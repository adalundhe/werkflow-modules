from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_trusted_access_program_summary import BedrockTrustedAccessProgramSummary


class BedrockListTrustedAccessProgramsResponse(BaseModel):
    programSummaries: list[BedrockTrustedAccessProgramSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
