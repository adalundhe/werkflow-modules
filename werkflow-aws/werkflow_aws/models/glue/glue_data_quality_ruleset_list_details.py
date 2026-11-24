from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_data_quality_target_table import GlueDataQualityTargetTable


class GlueDataQualityRulesetListDetails(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    CreatedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    TargetTable: GlueDataQualityTargetTable | None = None
    RecommendationRunId: StrictStr | None = None
    RuleCount: StrictInt | None = None
