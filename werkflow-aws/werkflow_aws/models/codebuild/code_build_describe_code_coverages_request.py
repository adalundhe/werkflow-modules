from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class CodeBuildDescribeCodeCoveragesRequest(BaseModel):
    reportArn: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    sortOrder: Literal['ASCENDING', 'DESCENDING'] | None = None
    sortBy: Literal['LINE_COVERAGE_PERCENTAGE', 'FILE_PATH'] | None = None
    minLineCoveragePercentage: StrictFloat | StrictInt | None = None
    maxLineCoveragePercentage: StrictFloat | StrictInt | None = None
