from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_validate_policy_finding import AccessAnalyzerValidatePolicyFinding


class AccessAnalyzerValidatePolicyResponse(BaseModel):
    findings: list[AccessAnalyzerValidatePolicyFinding] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
