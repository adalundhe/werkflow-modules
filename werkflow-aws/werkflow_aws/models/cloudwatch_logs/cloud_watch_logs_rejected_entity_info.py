from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsRejectedEntityInfo(BaseModel):
    errorType: StrictStr | None = None
