from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESSuppressedDestinationSummary(BaseModel):
    EmailAddress: StrictStr | None = None
    Reason: StrictStr | None = None
    LastUpdateTime: datetime.datetime | StrictStr | None = None
