from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .macie_resource_statistics import MacieResourceStatistics


class MacieGetResourceProfileResponse(BaseModel):
    profileUpdatedAt: datetime.datetime | StrictStr | None = None
    sensitivityScore: StrictInt | None = None
    sensitivityScoreOverridden: StrictBool | None = None
    statistics: MacieResourceStatistics | None = None
    ResponseMetadata: dict[str, Any] | None = None
