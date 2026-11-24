from __future__ import annotations
from pydantic import BaseModel, StrictStr


class FSxCancelDataRepositoryTaskRequest(BaseModel):
    TaskId: StrictStr
