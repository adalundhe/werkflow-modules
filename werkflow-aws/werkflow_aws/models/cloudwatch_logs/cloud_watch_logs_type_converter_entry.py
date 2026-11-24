from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsTypeConverterEntry(BaseModel):
    key: StrictStr | None = None
    type: StrictStr | None = None
