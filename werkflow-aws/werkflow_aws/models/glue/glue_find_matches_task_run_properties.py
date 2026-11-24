from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueFindMatchesTaskRunProperties(BaseModel):
    JobId: StrictStr | None = None
    JobName: StrictStr | None = None
    JobRunId: StrictStr | None = None
