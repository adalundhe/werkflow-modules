from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_url import AuditManagerURL


class AuditManagerGetAssessmentReportUrlResponse(BaseModel):
    preSignedUrl: AuditManagerURL | None = None
    ResponseMetadata: dict[str, Any] | None = None
