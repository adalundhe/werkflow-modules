from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr


class EC2IdFormat(BaseModel):
    Deadline: datetime.datetime | StrictStr | None = None
    Resource: StrictStr | None = None
    UseLongIds: StrictBool | None = None
