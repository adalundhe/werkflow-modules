from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightUploadedDocumentMetadata(BaseModel):
    Name: StrictStr | None = None
