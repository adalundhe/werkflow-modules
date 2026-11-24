from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .config_service_conformance_pack_evaluation_result import ConfigServiceConformancePackEvaluationResult


class ConfigServiceGetConformancePackComplianceDetailsResponse(BaseModel):
    ConformancePackName: StrictStr | None = None
    ConformancePackRuleEvaluationResults: list[ConfigServiceConformancePackEvaluationResult] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
