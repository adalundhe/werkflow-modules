from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDeleteDocument(BaseModel):
    documentId: StrictStr
