from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DataZoneTimeSeriesDataPointFormInput(BaseModel):
    formName: StrictStr
    typeIdentifier: StrictStr
    timestamp: datetime.datetime | StrictStr
    typeRevision: StrictStr | None = None
    content: StrictStr | None = None
