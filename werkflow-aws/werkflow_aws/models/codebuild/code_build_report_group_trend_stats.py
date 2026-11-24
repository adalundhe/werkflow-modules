from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildReportGroupTrendStats(BaseModel):
    average: StrictStr | None = None
    max: StrictStr | None = None
    min: StrictStr | None = None
