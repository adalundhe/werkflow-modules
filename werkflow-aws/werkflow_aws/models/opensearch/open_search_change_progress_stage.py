from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class OpenSearchChangeProgressStage(BaseModel):
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Description: StrictStr | None = None
    LastUpdated: datetime.datetime | StrictStr | None = None
