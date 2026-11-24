from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeBuildTestReportSummary(BaseModel):
    total: StrictInt | None = None
    statusCounts: dict[StrictStr, StrictInt] | None = None
    durationInNanoSeconds: StrictInt | None = None
