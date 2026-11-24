from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .bedrock_project_summary import BedrockProjectSummary


class BedrockListProjectsResponse(BaseModel):
    projectSummaries: list[BedrockProjectSummary] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
