from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class DataPipelineSetTaskStatusRequest(BaseModel):
    taskId: StrictStr
    taskStatus: Literal['FINISHED', 'FAILED', 'FALSE']
    errorId: StrictStr | None = None
    errorMessage: StrictStr | None = None
    errorStackTrace: StrictStr | None = None
