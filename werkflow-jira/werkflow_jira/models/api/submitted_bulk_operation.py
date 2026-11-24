from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SubmittedBulkOperation(BaseModel):
    taskId: StrictStr | None = None
