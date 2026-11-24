from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailRelationalDatabaseEvent(BaseModel):
    resource: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    message: StrictStr | None = None
    eventCategories: list[StrictStr] | None = None
