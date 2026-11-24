from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSDaemonTaskDefinitionSummary(BaseModel):
    arn: StrictStr | None = None
    registeredAt: datetime.datetime | StrictStr | None = None
    registeredBy: StrictStr | None = None
    deleteRequestedAt: datetime.datetime | StrictStr | None = None
    status: StrictStr | None = None
