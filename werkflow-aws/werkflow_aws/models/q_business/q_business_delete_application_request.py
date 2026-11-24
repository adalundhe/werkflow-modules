from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteApplicationRequest(BaseModel):
    applicationId: StrictStr
