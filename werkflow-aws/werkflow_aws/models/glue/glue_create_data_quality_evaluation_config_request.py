from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_data_quality_evaluation_config_additional_run_options import GlueDataQualityEvaluationConfigAdditionalRunOptions
from .glue_data_quality_evaluation_config_data_source import GlueDataQualityEvaluationConfigDataSource
from .glue_data_source import GlueDataSource


class GlueCreateDataQualityEvaluationConfigRequest(BaseModel):
    Name: StrictStr
    Level: Literal['CATALOG', 'DATABASE', 'TABLE']
    DataSource: GlueDataQualityEvaluationConfigDataSource
    Role: StrictStr
    RulesetName: StrictStr | None = None
    ManagedRulesetName: Literal['SIMPLE', 'ADVANCED'] | None = None
    Triggers: list[Literal['ONCE', 'SCHEDULE', 'METADATA_CHANGE']] | None = None
    ScheduleExpression: StrictStr | None = None
    StartAt: datetime.datetime | StrictStr | None = None
    EndAt: datetime.datetime | StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    Timeout: StrictInt | None = None
    AdditionalRunOptions: GlueDataQualityEvaluationConfigAdditionalRunOptions | None = None
    AdditionalDataSources: dict[StrictStr, GlueDataSource] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    ClientToken: StrictStr | None = None
