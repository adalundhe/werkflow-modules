from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsSessionStreamingException(BaseModel):
    message: StrictStr | None = None
