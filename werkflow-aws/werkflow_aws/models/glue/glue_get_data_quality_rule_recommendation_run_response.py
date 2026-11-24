from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_data_quality_rule_recommendation_run_additional_run_options import GlueDataQualityRuleRecommendationRunAdditionalRunOptions
from .glue_data_source import GlueDataSource


class GlueGetDataQualityRuleRecommendationRunResponse(BaseModel):
    RunId: StrictStr | None = None
    DataSource: GlueDataSource | None = None
    Role: StrictStr | None = None
    NumberOfWorkers: StrictInt | None = None
    Timeout: StrictInt | None = None
    Status: StrictStr | None = None
    ErrorString: StrictStr | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    CompletedOn: datetime.datetime | StrictStr | None = None
    ExecutionTime: StrictInt | None = None
    RecommendedRuleset: StrictStr | None = None
    CreatedRulesetName: StrictStr | None = None
    DataQualitySecurityConfiguration: StrictStr | None = None
    AdditionalRunOptions: GlueDataQualityRuleRecommendationRunAdditionalRunOptions | None = None
    RecommendationMode: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
