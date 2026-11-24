from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class FISExperimentTemplateSummary(BaseModel):
    id: StrictStr | None = None
    arn: StrictStr | None = None
    description: StrictStr | None = None
    creationTime: datetime.datetime | StrictStr | None = None
    lastUpdateTime: datetime.datetime | StrictStr | None = None
    tags: dict[StrictStr, StrictStr] | None = None
