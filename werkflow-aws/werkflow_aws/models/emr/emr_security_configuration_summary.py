from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EMRSecurityConfigurationSummary(BaseModel):
    Name: StrictStr | None = None
    CreationDateTime: datetime.datetime | StrictStr | None = None
