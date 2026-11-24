from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_data_quality_rule_recommendation_run_description import GlueDataQualityRuleRecommendationRunDescription


class GlueListDataQualityRuleRecommendationRunsResponse(BaseModel):
    Runs: list[GlueDataQualityRuleRecommendationRunDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
