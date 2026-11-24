from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CloudWatchLogsSplitStringEntry(BaseModel):
    source: StrictStr | None = None
    delimiter: StrictStr | None = None
