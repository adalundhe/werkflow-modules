from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGetIndexRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
