from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class LightsailInstanceHealthStatusDetail(BaseModel):
    name: StrictStr | None = None
    status: StrictStr | None = None
    impairedSince: datetime.datetime | StrictStr | None = None
