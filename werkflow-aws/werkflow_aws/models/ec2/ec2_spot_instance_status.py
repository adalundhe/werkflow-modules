from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2SpotInstanceStatus(BaseModel):
    Code: StrictStr | None = None
    Message: StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
