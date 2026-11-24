from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueGetJobBookmarkRequest(BaseModel):
    JobName: StrictStr
    RunId: StrictStr | None = None
