from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectCustomerVoiceActivity(BaseModel):
    GreetingStartTimestamp: datetime.datetime | StrictStr | None = None
    GreetingEndTimestamp: datetime.datetime | StrictStr | None = None
