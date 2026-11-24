from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsParseVPC(BaseModel):
    source: StrictStr | None = None
