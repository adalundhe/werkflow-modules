from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EventBridgePartnerEventSourceAccount(BaseModel):
    Account: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    ExpirationTime: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
