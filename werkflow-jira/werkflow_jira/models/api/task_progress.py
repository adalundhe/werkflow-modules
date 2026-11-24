from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr


class TaskProgress(BaseModel):
    description: StrictStr | None = None
    elapsedRuntime: StrictInt | None = None
    finished: StrictStr | None = None
    id: StrictStr | None = None
    lastUpdate: StrictStr | None = None
    message: StrictStr | None = None
    progress: StrictInt | None = None
    result: Any = None
    self: StrictStr | None = None
    started: StrictStr | None = None
    status: StrictStr | None = None
    submitted: StrictStr | None = None
    submittedBy: StrictInt | None = None
