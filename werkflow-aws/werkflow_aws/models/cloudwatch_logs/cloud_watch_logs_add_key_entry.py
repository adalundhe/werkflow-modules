from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsAddKeyEntry(BaseModel):
    key: StrictStr | None = None
    value: StrictStr | None = None
    overwriteIfExists: StrictBool | None = None
