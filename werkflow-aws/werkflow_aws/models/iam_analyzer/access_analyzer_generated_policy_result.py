from __future__ import annotations
from pydantic import BaseModel
from .access_analyzer_generated_policy import AccessAnalyzerGeneratedPolicy
from .access_analyzer_generated_policy_properties import AccessAnalyzerGeneratedPolicyProperties


class AccessAnalyzerGeneratedPolicyResult(BaseModel):
    properties: AccessAnalyzerGeneratedPolicyProperties | None = None
    generatedPolicies: list[AccessAnalyzerGeneratedPolicy] | None = None
