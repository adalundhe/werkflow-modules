from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSCreatedAt(BaseModel):
    before: datetime.datetime | StrictStr | None = None
    after: datetime.datetime | StrictStr | None = None
