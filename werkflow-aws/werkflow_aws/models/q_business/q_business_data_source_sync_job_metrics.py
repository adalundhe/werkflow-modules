from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDataSourceSyncJobMetrics(BaseModel):
    documentsAdded: StrictStr | None = None
    documentsModified: StrictStr | None = None
    documentsDeleted: StrictStr | None = None
    documentsFailed: StrictStr | None = None
    documentsScanned: StrictStr | None = None
