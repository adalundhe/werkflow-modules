from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsSessionTimeoutException(BaseModel):
    message: StrictStr | None = None
