from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsInternalStreamingException(BaseModel):
    message: StrictStr | None = None
