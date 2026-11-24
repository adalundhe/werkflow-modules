from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueBatchStopJobRunSuccessfulSubmission(BaseModel):
    JobName: StrictStr | None = None
    JobRunId: StrictStr | None = None
