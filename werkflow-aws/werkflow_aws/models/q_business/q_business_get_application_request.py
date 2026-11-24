from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGetApplicationRequest(BaseModel):
    applicationId: StrictStr
