from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_data_source import GlueDataSource


class GlueDataQualityResultDescription(BaseModel):
    ResultId: StrictStr | None = None
    EvaluationRunMode: StrictStr | None = None
    DataQualityEvaluationConfig: StrictStr | None = None
    DataSource: GlueDataSource | None = None
    JobName: StrictStr | None = None
    JobRunId: StrictStr | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
