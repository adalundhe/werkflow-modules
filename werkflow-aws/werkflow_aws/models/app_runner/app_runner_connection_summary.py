from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class AppRunnerConnectionSummary(BaseModel):
    ConnectionName: StrictStr | None = None
    ConnectionArn: StrictStr | None = None
    ProviderType: StrictStr | None = None
    Status: StrictStr | None = None
    CreatedAt: datetime.datetime | StrictStr | None = None
