from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class BatchContainerSummary(BaseModel):
    exitCode: StrictInt | None = None
    reason: StrictStr | None = None
