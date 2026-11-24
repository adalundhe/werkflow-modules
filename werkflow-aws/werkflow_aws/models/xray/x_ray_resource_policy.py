from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class XRayResourcePolicy(BaseModel):
    PolicyName: StrictStr | None = None
    PolicyDocument: StrictStr | None = None
    PolicyRevisionId: StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
