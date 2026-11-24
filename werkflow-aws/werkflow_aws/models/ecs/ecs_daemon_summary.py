from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSDaemonSummary(BaseModel):
    daemonArn: StrictStr | None = None
    status: StrictStr | None = None
    createdAt: datetime.datetime | StrictStr | None = None
    updatedAt: datetime.datetime | StrictStr | None = None
