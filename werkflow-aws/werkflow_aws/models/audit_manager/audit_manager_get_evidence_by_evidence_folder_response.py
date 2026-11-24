from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .audit_manager_evidence import AuditManagerEvidence


class AuditManagerGetEvidenceByEvidenceFolderResponse(BaseModel):
    evidence: list[AuditManagerEvidence] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
