from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .glue_data_quality_evaluation_config_additional_run_options import GlueDataQualityEvaluationConfigAdditionalRunOptions
from .glue_data_quality_evaluation_config_data_source import GlueDataQualityEvaluationConfigDataSource
from .glue_data_source import GlueDataSource


class GlueGetDataQualityEvaluationConfigResponse(BaseModel):
    Name: StrictStr | None = None
    EvaluationRunMode: StrictStr | None = None
    CreatedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    Level: StrictStr | None = None
    DataSource: GlueDataQualityEvaluationConfigDataSource | None = None
    RulesetName: StrictStr | None = None
    ManagedRulesetName: StrictStr | None = None
    Triggers: list[StrictStr] | None = None
    ScheduleExpression: StrictStr | None = None
    StartAt: datetime.datetime | StrictStr | None = None
    EndAt: datetime.datetime | StrictStr | None = None
    PauseRuns: StrictBool | None = None
    Role: StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    Timeout: StrictInt | None = None
    AdditionalRunOptions: GlueDataQualityEvaluationConfigAdditionalRunOptions | None = None
    AdditionalDataSources: dict[StrictStr, GlueDataSource] | None = None
    ResponseMetadata: dict[str, Any] | None = None
