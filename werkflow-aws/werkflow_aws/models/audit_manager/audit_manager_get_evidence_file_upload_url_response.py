from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class AuditManagerGetEvidenceFileUploadUrlResponse(BaseModel):
    evidenceFileName: StrictStr | None = None
    uploadUrl: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
