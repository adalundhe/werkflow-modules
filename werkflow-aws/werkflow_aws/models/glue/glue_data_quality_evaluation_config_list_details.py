from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_data_quality_evaluation_config_list_data_source import GlueDataQualityEvaluationConfigListDataSource


class GlueDataQualityEvaluationConfigListDetails(BaseModel):
    Name: StrictStr | None = None
    EvaluationRunMode: StrictStr | None = None
    CreatedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    Level: StrictStr | None = None
    DataSource: GlueDataQualityEvaluationConfigListDataSource | None = None
    RulesetName: StrictStr | None = None
    ManagedRulesetName: StrictStr | None = None
    PauseRuns: StrictBool | None = None
