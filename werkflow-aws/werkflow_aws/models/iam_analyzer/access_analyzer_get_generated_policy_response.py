from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .access_analyzer_generated_policy_result import AccessAnalyzerGeneratedPolicyResult
from .access_analyzer_job_details import AccessAnalyzerJobDetails


class AccessAnalyzerGetGeneratedPolicyResponse(BaseModel):
    jobDetails: AccessAnalyzerJobDetails | None = None
    generatedPolicyResult: AccessAnalyzerGeneratedPolicyResult | None = None
    ResponseMetadata: dict[str, Any] | None = None
