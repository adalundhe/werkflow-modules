from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsParseRoute53(BaseModel):
    source: StrictStr | None = None
