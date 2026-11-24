from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsOpenSearchResourceStatus(BaseModel):
    status: StrictStr | None = None
    statusMessage: StrictStr | None = None
