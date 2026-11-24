from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteIndexRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
