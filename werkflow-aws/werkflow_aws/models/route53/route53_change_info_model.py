from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class Route53ChangeInfoModel(BaseModel):
    Id: StrictStr | None = None
    Status: StrictStr | None = None
    SubmittedAt: datetime.datetime | StrictStr | None = None
    Comment: StrictStr | None = None
