from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerManualEvidence(BaseModel):
    s3ResourcePath: StrictStr | None = None
    textResponse: StrictStr | None = None
    evidenceFileName: StrictStr | None = None
