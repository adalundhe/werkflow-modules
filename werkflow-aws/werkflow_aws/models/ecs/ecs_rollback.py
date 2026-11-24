from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSRollback(BaseModel):
    reason: StrictStr | None = None
    startedAt: datetime.datetime | StrictStr | None = None
    serviceRevisionArn: StrictStr | None = None
