from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchInsight(BaseModel):
    InsightId: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Type: StrictStr | None = None
    Priority: StrictStr | None = None
    Status: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
    IsExperimental: StrictBool | None = None
