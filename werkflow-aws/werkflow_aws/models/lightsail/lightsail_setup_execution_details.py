from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailSetupExecutionDetails(BaseModel):
    command: StrictStr | None = None
    dateTime: datetime.datetime | StrictStr | None = None
    name: StrictStr | None = None
    status: StrictStr | None = None
    standardError: StrictStr | None = None
    standardOutput: StrictStr | None = None
    version: StrictStr | None = None
