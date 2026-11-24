from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMUpdateDocumentDefaultVersionRequest(BaseModel):
    Name: StrictStr
    DocumentVersion: StrictStr
