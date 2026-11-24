from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGetDataAccessorRequest(BaseModel):
    applicationId: StrictStr
    dataAccessorId: StrictStr
