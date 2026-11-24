from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchTerminateServiceJobsErrorDetail(BaseModel):
    job: StrictStr | None = None
    code: StrictStr | None = None
    message: StrictStr | None = None
