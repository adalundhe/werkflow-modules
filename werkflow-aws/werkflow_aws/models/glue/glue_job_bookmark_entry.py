from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueJobBookmarkEntry(BaseModel):
    JobName: StrictStr | None = None
    Version: StrictInt | None = None
    Run: StrictInt | None = None
    Attempt: StrictInt | None = None
    PreviousRunId: StrictStr | None = None
    RunId: StrictStr | None = None
    JobBookmark: StrictStr | None = None
