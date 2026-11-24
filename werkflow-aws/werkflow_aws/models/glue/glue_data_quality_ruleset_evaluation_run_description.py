from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_data_source import GlueDataSource


class GlueDataQualityRulesetEvaluationRunDescription(BaseModel):
    RunId: StrictStr | None = None
    Status: StrictStr | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
    DataSource: GlueDataSource | None = None
