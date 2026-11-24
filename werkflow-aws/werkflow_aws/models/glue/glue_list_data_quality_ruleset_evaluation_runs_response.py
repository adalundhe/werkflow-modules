from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_data_quality_ruleset_evaluation_run_description import GlueDataQualityRulesetEvaluationRunDescription


class GlueListDataQualityRulesetEvaluationRunsResponse(BaseModel):
    Runs: list[GlueDataQualityRulesetEvaluationRunDescription] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
