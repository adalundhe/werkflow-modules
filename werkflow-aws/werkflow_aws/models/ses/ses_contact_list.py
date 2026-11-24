from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESContactList(BaseModel):
    ContactListName: StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
