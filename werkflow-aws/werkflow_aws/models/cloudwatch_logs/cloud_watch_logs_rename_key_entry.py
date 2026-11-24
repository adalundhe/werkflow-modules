from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsRenameKeyEntry(BaseModel):
    key: StrictStr | None = None
    renameTo: StrictStr | None = None
    overwriteIfExists: StrictBool | None = None
