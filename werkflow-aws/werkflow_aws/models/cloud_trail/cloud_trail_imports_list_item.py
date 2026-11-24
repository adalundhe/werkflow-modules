from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudTrailImportsListItem(BaseModel):
    ImportId: StrictStr | None = None
    ImportStatus: StrictStr | None = None
    Destinations: list[StrictStr] | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    UpdatedTimestamp: datetime.datetime | StrictStr | None = None
