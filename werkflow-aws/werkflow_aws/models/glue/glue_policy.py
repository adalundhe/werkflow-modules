from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class GluePolicy(BaseModel):
    PolicyInJson: StrictStr | None = None
    PolicyHash: StrictStr | None = None
    CreateTime: datetime.datetime | StrictStr | None = None
    UpdateTime: datetime.datetime | StrictStr | None = None
