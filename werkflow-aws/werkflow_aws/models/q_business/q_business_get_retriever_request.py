from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessGetRetrieverRequest(BaseModel):
    applicationId: StrictStr
    retrieverId: StrictStr
