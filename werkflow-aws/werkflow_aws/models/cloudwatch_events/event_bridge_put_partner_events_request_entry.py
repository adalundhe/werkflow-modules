from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EventBridgePutPartnerEventsRequestEntry(BaseModel):
    Time: datetime.datetime | StrictStr | None = None
    Source: StrictStr | None = None
    Resources: list[StrictStr] | None = None
    DetailType: StrictStr | None = None
    Detail: StrictStr | None = None
