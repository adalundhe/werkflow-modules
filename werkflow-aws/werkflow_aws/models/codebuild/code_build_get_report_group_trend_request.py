from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr


class CodeBuildGetReportGroupTrendRequest(BaseModel):
    reportGroupArn: StrictStr
    trendField: Literal['PASS_RATE', 'DURATION', 'TOTAL', 'LINE_COVERAGE', 'LINES_COVERED', 'LINES_MISSED', 'BRANCH_COVERAGE', 'BRANCHES_COVERED', 'BRANCHES_MISSED']
    numOfReports: StrictInt | None = None
