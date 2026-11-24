from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .glue_data_quality_aggregated_metrics import GlueDataQualityAggregatedMetrics
from .glue_data_quality_analyzer_result import GlueDataQualityAnalyzerResult
from .glue_data_quality_observation import GlueDataQualityObservation
from .glue_data_quality_rule_result import GlueDataQualityRuleResult
from .glue_data_source import GlueDataSource


class GlueGetDataQualityResultResponse(BaseModel):
    ResultId: StrictStr | None = None
    EvaluationRunMode: StrictStr | None = None
    DataQualityEvaluationConfig: StrictStr | None = None
    ProfileId: StrictStr | None = None
    Score: StrictFloat | StrictInt | None = None
    DataSource: GlueDataSource | None = None
    RulesetName: StrictStr | None = None
    EvaluationContext: StrictStr | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
    CompletedOn: datetime.datetime | StrictStr | None = None
    JobName: StrictStr | None = None
    JobRunId: StrictStr | None = None
    RulesetEvaluationRunId: StrictStr | None = None
    RuleResults: list[GlueDataQualityRuleResult] | None = None
    AnalyzerResults: list[GlueDataQualityAnalyzerResult] | None = None
    Observations: list[GlueDataQualityObservation] | None = None
    AggregatedMetrics: GlueDataQualityAggregatedMetrics | None = None
    ResponseMetadata: dict[str, Any] | None = None
