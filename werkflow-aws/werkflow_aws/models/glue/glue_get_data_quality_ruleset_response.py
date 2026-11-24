from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_data_quality_target_table import GlueDataQualityTargetTable


class GlueGetDataQualityRulesetResponse(BaseModel):
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    Ruleset: StrictStr | None = None
    TargetTable: GlueDataQualityTargetTable | None = None
    CreatedOn: datetime.datetime | StrictStr | None = None
    LastModifiedOn: datetime.datetime | StrictStr | None = None
    RecommendationRunId: StrictStr | None = None
    DataQualitySecurityConfiguration: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
