from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMScheduledWindowExecution(BaseModel):
    WindowId: StrictStr | None = None
    Name: StrictStr | None = None
    ExecutionTime: StrictStr | None = None
