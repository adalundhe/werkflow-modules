from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_data_quality_rule_results_options import GlueDataQualityRuleResultsOptions
from .glue_observation_results_options import GlueObservationResultsOptions
from .glue_profiling_results_options import GlueProfilingResultsOptions
from .glue_row_level_results_options import GlueRowLevelResultsOptions


class GlueDataQualityEvaluationConfigAdditionalRunOptions(BaseModel):
    CloudWatchMetricsEnabled: StrictBool | None = None
    ResultsS3Prefix: StrictStr | None = None
    CompositeRuleEvaluationMethod: StrictStr | None = None
    RowLevelResults: GlueRowLevelResultsOptions | None = None
    ProfilingResults: GlueProfilingResultsOptions | None = None
    ObservationScope: StrictStr | None = None
    ObservationMode: StrictStr | None = None
    DataQualityRuleResults: GlueDataQualityRuleResultsOptions | None = None
    ObservationResults: GlueObservationResultsOptions | None = None
    CustomLogGroupPrefix: StrictStr | None = None
