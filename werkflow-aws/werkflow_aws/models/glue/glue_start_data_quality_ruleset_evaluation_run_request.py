from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_data_quality_evaluation_run_additional_run_options import GlueDataQualityEvaluationRunAdditionalRunOptions
from .glue_data_source import GlueDataSource


class GlueStartDataQualityRulesetEvaluationRunRequest(BaseModel):
    DataSource: GlueDataSource
    Role: StrictStr
    RulesetNames: list[StrictStr]
    NumberOfWorkers: StrictInt | None = None
    Timeout: StrictInt | None = None
    ClientToken: StrictStr | None = None
    AdditionalRunOptions: GlueDataQualityEvaluationRunAdditionalRunOptions | None = None
    AdditionalDataSources: dict[StrictStr, GlueDataSource] | None = None
