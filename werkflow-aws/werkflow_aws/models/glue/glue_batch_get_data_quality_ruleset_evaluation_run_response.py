from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_data_quality_ruleset_evaluation_run import GlueDataQualityRulesetEvaluationRun


class GlueBatchGetDataQualityRulesetEvaluationRunResponse(BaseModel):
    Runs: list[GlueDataQualityRulesetEvaluationRun] | None = None
    RunsNotFound: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
