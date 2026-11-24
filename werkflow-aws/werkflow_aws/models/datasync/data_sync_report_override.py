from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DataSyncReportOverride(BaseModel):
    ReportLevel: StrictStr | None = None
