from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .audit_manager_evidence import AuditManagerEvidence


class AuditManagerGetEvidenceResponse(BaseModel):
    evidence: AuditManagerEvidence | None = None
    ResponseMetadata: dict[str, Any] | None = None
