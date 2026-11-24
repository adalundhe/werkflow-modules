from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSStopTaskRequest(BaseModel):
    task: StrictStr
    cluster: StrictStr | None = None
    reason: StrictStr | None = None
