from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class QBusinessGetDocumentContentRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    documentId: StrictStr
    dataSourceId: StrictStr | None = None
    outputFormat: Literal['RAW', 'EXTRACTED'] | None = None
