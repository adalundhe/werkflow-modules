from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_data_source import GlueDataSource


class GlueDataQualityRuleRecommendationRunDescription(BaseModel):
    RunId: StrictStr | None = None
    Status: StrictStr | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
    DataSource: GlueDataSource | None = None
    CreatedRulesetName: StrictStr | None = None
    RecommendationMode: StrictStr | None = None
