from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class QuickSightAnalysisSummary(BaseModel):
    Arn: StrictStr | None = None
    AnalysisId: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
