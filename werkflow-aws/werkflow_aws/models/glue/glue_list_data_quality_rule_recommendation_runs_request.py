from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_data_quality_rule_recommendation_run_filter import GlueDataQualityRuleRecommendationRunFilter


class GlueListDataQualityRuleRecommendationRunsRequest(BaseModel):
    Filter: GlueDataQualityRuleRecommendationRunFilter | None = None
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
