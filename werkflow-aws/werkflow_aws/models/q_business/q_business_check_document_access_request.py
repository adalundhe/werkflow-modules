from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessCheckDocumentAccessRequest(BaseModel):
    applicationId: StrictStr
    indexId: StrictStr
    userId: StrictStr
    documentId: StrictStr
    dataSourceId: StrictStr | None = None
