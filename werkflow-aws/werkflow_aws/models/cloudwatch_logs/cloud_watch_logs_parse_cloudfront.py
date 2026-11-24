from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsParseCloudfront(BaseModel):
    source: StrictStr | None = None
