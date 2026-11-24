from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EMRStudioSummary(BaseModel):
    StudioId: StrictStr | None = None
    Name: StrictStr | None = None
    VpcId: StrictStr | None = None
    Description: StrictStr | None = None
    Url: StrictStr | None = None
    AuthMode: StrictStr | None = None
    CreationTime: datetime.datetime | StrictStr | None = None
