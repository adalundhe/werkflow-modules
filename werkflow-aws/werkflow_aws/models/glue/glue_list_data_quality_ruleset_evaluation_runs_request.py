from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_data_quality_ruleset_evaluation_run_filter import GlueDataQualityRulesetEvaluationRunFilter


class GlueListDataQualityRulesetEvaluationRunsRequest(BaseModel):
    Filter: GlueDataQualityRulesetEvaluationRunFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
