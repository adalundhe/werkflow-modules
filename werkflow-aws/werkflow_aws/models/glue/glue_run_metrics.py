from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueRunMetrics(BaseModel):
    NumberOfBytesCompacted: StrictStr | None = None
    NumberOfFilesCompacted: StrictStr | None = None
    NumberOfDpus: StrictStr | None = None
    JobDurationInHour: StrictStr | None = None
