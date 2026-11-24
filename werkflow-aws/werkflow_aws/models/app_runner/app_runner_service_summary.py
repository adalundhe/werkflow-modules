from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AppRunnerServiceSummary(BaseModel):
    ServiceName: StrictStr | None = None
    ServiceId: StrictStr | None = None
    ServiceArn: StrictStr | None = None
    ServiceUrl: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
    UpdatedAt: datetime.datetime | StrictStr | None = None
    Status: StrictStr | None = None
