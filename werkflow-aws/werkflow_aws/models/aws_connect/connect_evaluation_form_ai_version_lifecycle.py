from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConnectEvaluationFormAIVersionLifecycle(BaseModel):
    Status: StrictStr | None = None
    StartOfLifeTime: datetime.datetime | StrictStr | None = None
    EndOfLifeTime: datetime.datetime | StrictStr | None = None
