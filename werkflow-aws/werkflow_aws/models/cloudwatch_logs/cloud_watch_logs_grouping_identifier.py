from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsGroupingIdentifier(BaseModel):
    key: StrictStr | None = None
    value: StrictStr | None = None
