from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class GlueStatisticModelResult(BaseModel):
    LowerBound: StrictFloat | StrictInt | None = None
    UpperBound: StrictFloat | StrictInt | None = None
    PredictedValue: StrictFloat | StrictInt | None = None
    ActualValue: StrictFloat | StrictInt | None = None
    Date: datetime.datetime | StrictStr | None = None
    InclusionAnnotation: StrictStr | None = None
