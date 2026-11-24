from __future__ import annotations
from pydantic import BaseModel, StrictStr


class KendraDataSourceSyncJobMetrics(BaseModel):
    DocumentsAdded: StrictStr | None = None
    DocumentsModified: StrictStr | None = None
    DocumentsDeleted: StrictStr | None = None
    DocumentsFailed: StrictStr | None = None
    DocumentsScanned: StrictStr | None = None
