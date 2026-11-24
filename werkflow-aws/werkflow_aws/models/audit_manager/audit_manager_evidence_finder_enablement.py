from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerEvidenceFinderEnablement(BaseModel):
    eventDataStoreArn: StrictStr | None = None
    enablementStatus: StrictStr | None = None
    backfillStatus: StrictStr | None = None
    error: StrictStr | None = None
