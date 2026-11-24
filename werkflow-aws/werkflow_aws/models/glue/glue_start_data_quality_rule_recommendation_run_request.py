from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_data_quality_rule_recommendation_run_additional_run_options import GlueDataQualityRuleRecommendationRunAdditionalRunOptions
from .glue_data_source import GlueDataSource


class GlueStartDataQualityRuleRecommendationRunRequest(BaseModel):
    DataSource: GlueDataSource
    Role: StrictStr
    NumberOfWorkers: StrictInt | None = None
    Timeout: StrictInt | None = None
    CreatedRulesetName: StrictStr | None = None
    DataQualitySecurityConfiguration: StrictStr | None = None
    ClientToken: StrictStr | None = None
    AdditionalRunOptions: GlueDataQualityRuleRecommendationRunAdditionalRunOptions | None = None
    RecommendationMode: Literal['BASIC', 'ADVANCED'] | None = None
