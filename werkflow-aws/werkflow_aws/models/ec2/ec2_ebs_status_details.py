from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2EbsStatusDetails(BaseModel):
    ImpairedSince: datetime.datetime | StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
