from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneTimeSeriesDataPointFormOutput(BaseModel):
    formName: StrictStr | None = None
    typeIdentifier: StrictStr | None = None
    typeRevision: StrictStr | None = None
    timestamp: datetime.datetime | StrictStr | None = None
    content: StrictStr | None = None
    id: StrictStr | None = None
