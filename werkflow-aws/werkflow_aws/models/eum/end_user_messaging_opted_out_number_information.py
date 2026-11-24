from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class EndUserMessagingOptedOutNumberInformation(BaseModel):
    OptedOutNumber: StrictStr | None = None
    OptedOutTimestamp: datetime.datetime | StrictStr | None = None
    EndUserOptedOut: StrictBool | None = None
