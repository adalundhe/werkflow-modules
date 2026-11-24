from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class NeptuneEvent(BaseModel):
    SourceIdentifier: StrictStr | None = None
    SourceType: StrictStr | None = None
    Message: StrictStr | None = None
    EventCategories: list[StrictStr] | None = None
    Date: datetime.datetime | StrictStr | None = None
    SourceArn: StrictStr | None = None
