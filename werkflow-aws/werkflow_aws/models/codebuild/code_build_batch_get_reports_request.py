from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildBatchGetReportsRequest(BaseModel):
    reportArns: list[StrictStr]
