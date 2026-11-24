from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .glue_data_quality_aggregated_metrics import GlueDataQualityAggregatedMetrics
from .glue_data_quality_analyzer_result import GlueDataQualityAnalyzerResult
from .glue_data_quality_observation import GlueDataQualityObservation
from .glue_data_quality_rule_result import GlueDataQualityRuleResult
from .glue_data_source import GlueDataSource


class GlueGetDataQualityResultV2Response(BaseModel):
    ResultId: StrictStr | None = None
    EvaluationRunMode: StrictStr | None = None
    DataQualityEvaluationConfig: StrictStr | None = None
    DataSource: GlueDataSource | None = None
    ProfileId: StrictStr | None = None
    Dimensions: dict[StrictStr, StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ExecutionStartedOn: datetime.datetime | StrictStr | None = None
    ExecutionCompletedOn: datetime.datetime | StrictStr | None = None
    ResultPublishedOn: datetime.datetime | StrictStr | None = None
    Score: StrictFloat | StrictInt | None = None
    RuleResults: list[GlueDataQualityRuleResult] | None = None
    AnalyzerResults: list[GlueDataQualityAnalyzerResult] | None = None
    Observations: list[GlueDataQualityObservation] | None = None
    EvaluationContext: StrictStr | None = None
    Descriptors: dict[StrictStr, StrictStr] | None = None
    AggregatedMetrics: GlueDataQualityAggregatedMetrics | None = None
    RulesetName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
