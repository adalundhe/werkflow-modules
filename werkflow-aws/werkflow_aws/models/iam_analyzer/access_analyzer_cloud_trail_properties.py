from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .access_analyzer_trail_properties import AccessAnalyzerTrailProperties


class AccessAnalyzerCloudTrailProperties(BaseModel):
    trailProperties: list[AccessAnalyzerTrailProperties] | None = None
    startTime: datetime.datetime | StrictStr | None = None
    endTime: datetime.datetime | StrictStr | None = None
