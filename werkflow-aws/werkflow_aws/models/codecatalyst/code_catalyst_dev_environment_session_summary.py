from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodeCatalystDevEnvironmentSessionSummary(BaseModel):
    spaceName: StrictStr | None = None
    projectName: StrictStr | None = None
    devEnvironmentId: StrictStr | None = None
    startedTime: datetime.datetime | StrictStr | None = None
    id: StrictStr | None = None
