from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsRecordField(BaseModel):
    name: StrictStr | None = None
    mandatory: StrictBool | None = None
