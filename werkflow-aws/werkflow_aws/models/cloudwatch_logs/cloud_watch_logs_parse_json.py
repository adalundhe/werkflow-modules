from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsParseJSON(BaseModel):
    source: StrictStr | None = None
    destination: StrictStr | None = None
