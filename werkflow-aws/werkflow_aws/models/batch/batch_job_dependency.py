from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchJobDependency(BaseModel):
    jobId: StrictStr | None = None
    type: StrictStr | None = None
