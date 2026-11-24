from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneTimeSeriesDataPointSummaryFormOutput(BaseModel):
    formName: StrictStr | None = None
    typeIdentifier: StrictStr | None = None
    typeRevision: StrictStr | None = None
    timestamp: datetime.datetime | StrictStr | None = None
    contentSummary: StrictStr | None = None
    id: StrictStr | None = None
