from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CloudWatchLogsMoveKeyEntry(BaseModel):
    source: StrictStr | None = None
    target: StrictStr | None = None
    overwriteIfExists: StrictBool | None = None
