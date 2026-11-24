from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CodeBuildCodeCoverage(BaseModel):
    id: StrictStr | None = None
    reportARN: StrictStr | None = None
    filePath: StrictStr | None = None
    lineCoveragePercentage: StrictFloat | StrictInt | None = None
    linesCovered: StrictInt | None = None
    linesMissed: StrictInt | None = None
    branchCoveragePercentage: StrictFloat | StrictInt | None = None
    branchesCovered: StrictInt | None = None
    branchesMissed: StrictInt | None = None
    expired: datetime.datetime | StrictStr | None = None
