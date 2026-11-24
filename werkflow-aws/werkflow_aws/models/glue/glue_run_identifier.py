from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueRunIdentifier(BaseModel):
    RunId: StrictStr | None = None
    JobRunId: StrictStr | None = None
