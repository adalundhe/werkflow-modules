from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .access_analyzer_policy_generation import AccessAnalyzerPolicyGeneration


class AccessAnalyzerListPolicyGenerationsResponse(BaseModel):
    policyGenerations: list[AccessAnalyzerPolicyGeneration] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
