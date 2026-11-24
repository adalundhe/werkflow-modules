from __future__ import annotations
import datetime
from typing import Literal
from pydantic import BaseModel, StrictStr


class EMRListNotebookExecutionsRequest(BaseModel):
    EditorId: StrictStr | None = None
    Status: Literal['START_PENDING', 'STARTING', 'RUNNING', 'FINISHING', 'FINISHED', 'FAILING', 'FAILED', 'STOP_PENDING', 'STOPPING', 'STOPPED'] | None = None
    From: datetime.datetime | StrictStr | None = None
    To: datetime.datetime | StrictStr | None = None
    Marker: StrictStr | None = None
    ExecutionEngineId: StrictStr | None = None
