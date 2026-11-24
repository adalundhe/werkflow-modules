from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GlueDataQualityRuleResult(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    EvaluationMessage: StrictStr | None = None
    Result: StrictStr | None = None
    EvaluatedMetrics: dict[StrictStr, StrictFloat | StrictInt] | None = None
    EvaluatedRule: StrictStr | None = None
    RuleMetrics: dict[StrictStr, StrictFloat | StrictInt] | None = None
    Labels: dict[StrictStr, StrictStr] | None = None
