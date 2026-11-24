from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .glue_data_source import GlueDataSource


class GlueDataQualityResultsV2Description(BaseModel):
    ResultId: StrictStr | None = None
    EvaluationRunMode: StrictStr | None = None
    DataQualityEvaluationConfig: StrictStr | None = None
    DataSource: GlueDataSource | None = None
    ResultPublishedOn: datetime.datetime | StrictStr | None = None
    Dimensions: dict[StrictStr, StrictStr] | None = None
    EvaluationContext: StrictStr | None = None
    Descriptors: dict[StrictStr, StrictStr] | None = None
