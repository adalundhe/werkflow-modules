from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildBatchGetReportGroupsRequest(BaseModel):
    reportGroupArns: list[StrictStr]
