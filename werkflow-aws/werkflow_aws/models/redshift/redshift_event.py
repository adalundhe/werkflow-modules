from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class RedshiftEvent(BaseModel):
    SourceIdentifier: StrictStr | None = None
    SourceType: StrictStr | None = None
    Message: StrictStr | None = None
    EventCategories: list[StrictStr] | None = None
    Severity: StrictStr | None = None
    Date: datetime.datetime | StrictStr | None = None
    EventId: StrictStr | None = None
