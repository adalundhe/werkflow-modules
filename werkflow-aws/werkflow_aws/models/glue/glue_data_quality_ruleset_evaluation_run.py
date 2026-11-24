from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_data_quality_evaluation_run_additional_run_options import GlueDataQualityEvaluationRunAdditionalRunOptions
from .glue_data_source import GlueDataSource


class GlueDataQualityRulesetEvaluationRun(BaseModel):
    RunId: StrictStr | None = None
    DataSource: GlueDataSource | None = None
    Role: StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    Timeout: StrictInt | None = None
    AdditionalRunOptions: GlueDataQualityEvaluationRunAdditionalRunOptions | None = None
    Status: StrictStr | None = None
    ErrorString: StrictStr | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    CompletedOn: datetime.datetime | StrictStr | None = None
    ExecutionTime: StrictInt | None = None
    RulesetNames: list[StrictStr] | None = None
    ResultIds: list[StrictStr] | None = None
    AdditionalDataSources: dict[StrictStr, GlueDataSource] | None = None
