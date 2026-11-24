from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteRetrieverRequest(BaseModel):
    applicationId: StrictStr
    retrieverId: StrictStr
