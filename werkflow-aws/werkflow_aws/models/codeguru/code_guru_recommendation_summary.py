from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_guru_rule_metadata import CodeGuruRuleMetadata


class CodeGuruRecommendationSummary(BaseModel):
    FilePath: StrictStr | None = None
    RecommendationId: StrictStr | None = None
    StartLine: StrictInt | None = None
    EndLine: StrictInt | None = None
    Description: StrictStr | None = None
    RecommendationCategory: StrictStr | None = None
    RuleMetadata: CodeGuruRuleMetadata | None = None
    Severity: StrictStr | None = None
