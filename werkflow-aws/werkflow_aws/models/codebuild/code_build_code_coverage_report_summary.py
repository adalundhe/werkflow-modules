from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt


class CodeBuildCodeCoverageReportSummary(BaseModel):
    lineCoveragePercentage: StrictFloat | StrictInt | None = None
    linesCovered: StrictInt | None = None
    linesMissed: StrictInt | None = None
    branchCoveragePercentage: StrictFloat | StrictInt | None = None
    branchesCovered: StrictInt | None = None
    branchesMissed: StrictInt | None = None
