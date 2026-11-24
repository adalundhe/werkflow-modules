from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GlueCrawl(BaseModel):
    State: StrictStr | None = None
    StartedOn: datetime.datetime | StrictStr | None = None
    CompletedOn: datetime.datetime | StrictStr | None = None
    ErrorMessage: StrictStr | None = None
    LogGroup: StrictStr | None = None
    LogStream: StrictStr | None = None
