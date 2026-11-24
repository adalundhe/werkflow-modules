from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsResultField(BaseModel):
    field: StrictStr | None = None
    value: StrictStr | None = None
