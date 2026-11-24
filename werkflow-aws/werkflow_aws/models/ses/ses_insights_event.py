from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .ses_event_details import SESEventDetails


class SESInsightsEvent(BaseModel):
    Timestamp: datetime.datetime | StrictStr | None = None
    Type: StrictStr | None = None
    Details: SESEventDetails | None = None
