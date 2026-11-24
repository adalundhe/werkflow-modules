from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsQueryParameter(BaseModel):
    name: StrictStr | None = None
    defaultValue: StrictStr | None = None
    description: StrictStr | None = None
