from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGrok(BaseModel):
    source: StrictStr | None = None
    match: StrictStr | None = None
