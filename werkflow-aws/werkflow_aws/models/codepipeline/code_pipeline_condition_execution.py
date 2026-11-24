from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CodePipelineConditionExecution(BaseModel):
    status: StrictStr | None = None
    summary: StrictStr | None = None
    lastStatusChange: datetime.datetime | StrictStr | None = None
