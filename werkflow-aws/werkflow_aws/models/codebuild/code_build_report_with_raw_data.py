from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CodeBuildReportWithRawData(BaseModel):
    reportArn: StrictStr | None = None
    data: StrictStr | None = None
