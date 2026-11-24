from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .access_analyzer_trail import AccessAnalyzerTrail


class AccessAnalyzerCloudTrailDetails(BaseModel):
    trails: list[AccessAnalyzerTrail]
    accessRole: StrictStr
    startTime: datetime.datetime | StrictStr
    endTime: datetime.datetime | StrictStr | None = None
