from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsParseWAF(BaseModel):
    source: StrictStr | None = None
