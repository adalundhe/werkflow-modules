from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessRetrieverContentSource(BaseModel):
    retrieverId: StrictStr
