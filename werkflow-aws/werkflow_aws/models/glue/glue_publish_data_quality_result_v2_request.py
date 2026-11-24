from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .glue_data_quality_aggregated_metrics import GlueDataQualityAggregatedMetrics
from .glue_data_quality_analyzer_result import GlueDataQualityAnalyzerResult
from .glue_data_quality_configuration_v2 import GlueDataQualityConfigurationV2
from .glue_data_quality_observation import GlueDataQualityObservation
from .glue_data_quality_rule_result import GlueDataQualityRuleResult
from .glue_data_quality_telemetry import GlueDataQualityTelemetry
from .glue_statistic_summary import GlueStatisticSummary


class GluePublishDataQualityResultV2Request(BaseModel):
    Dimensions: dict[StrictStr, StrictStr]
    Score: StrictFloat | StrictInt
    RuleResults: list[GlueDataQualityRuleResult]
    EvaluationContext: StrictStr
    Tags: dict[StrictStr, StrictStr] | None = None
    ExecutionStartedOn: datetime.datetime | StrictStr | None = None
    ExecutionCompletedOn: datetime.datetime | StrictStr | None = None
    AnalyzerResults: list[GlueDataQualityAnalyzerResult] | None = None
    Observations: list[GlueDataQualityObservation] | None = None
    AggregatedMetrics: GlueDataQualityAggregatedMetrics | None = None
    Statistics: list[GlueStatisticSummary] | None = None
    RunConfiguration: GlueDataQualityConfigurationV2 | None = None
    ClientToken: StrictStr | None = None
    Descriptors: dict[StrictStr, StrictStr] | None = None
    RulesetName: StrictStr | None = None
    DataQualitySecurityConfiguration: StrictStr | None = None
    Telemetry: GlueDataQualityTelemetry | None = None
