from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class DetectiveInvestigationDetail(BaseModel):
    InvestigationId: StrictStr | None = None
    Severity: StrictStr | None = None
    Status: StrictStr | None = None
    State: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    EntityArn: StrictStr | None = None
    EntityType: StrictStr | None = None
