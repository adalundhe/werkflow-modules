from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_data_source import GlueDataSource


class GlueDataQualityResultFilterCriteria(BaseModel):
    DataSource: GlueDataSource | None = None
    JobName: StrictStr | None = None
    JobRunId: StrictStr | None = None
    StartedAfter: datetime.datetime | StrictStr | None = None
    StartedBefore: datetime.datetime | StrictStr | None = None
    EvaluationRunMode: Literal['ON_DEMAND', 'EVALUATION_CONFIG'] | None = None
    DataQualityEvaluationConfig: StrictStr | None = None
