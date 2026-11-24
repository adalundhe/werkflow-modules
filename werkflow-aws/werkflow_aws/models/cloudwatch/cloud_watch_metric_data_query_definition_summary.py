from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class CloudWatchMetricDataQueryDefinitionSummary(BaseModel):
    Id: StrictStr | None = None
    Path: StrictStr | None = None
    Type: StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
