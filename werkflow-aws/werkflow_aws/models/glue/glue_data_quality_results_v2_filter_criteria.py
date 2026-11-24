from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr
from .glue_data_source import GlueDataSource


class GlueDataQualityResultsV2FilterCriteria(BaseModel):
    DataSource: GlueDataSource | None = None
    PublishedAfter: datetime.datetime | StrictStr | None = None
    PublishedBefore: datetime.datetime | StrictStr | None = None
    Dimensions: dict[StrictStr, StrictStr] | None = None
    EvaluationContext: StrictStr | None = None
    EvaluationRunMode: Literal['ON_DEMAND', 'EVALUATION_CONFIG'] | None = None
    DataQualityEvaluationConfig: StrictStr | None = None
