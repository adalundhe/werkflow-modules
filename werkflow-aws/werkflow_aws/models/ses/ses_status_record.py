from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESStatusRecord(BaseModel):
    Status: StrictStr | None = None
    Cause: StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
