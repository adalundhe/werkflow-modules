from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteDataAccessorRequest(BaseModel):
    applicationId: StrictStr
    dataAccessorId: StrictStr
