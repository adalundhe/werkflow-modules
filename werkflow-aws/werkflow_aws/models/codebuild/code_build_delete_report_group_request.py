from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class CodeBuildDeleteReportGroupRequest(BaseModel):
    arn: StrictStr
    deleteReports: StrictBool | None = None
