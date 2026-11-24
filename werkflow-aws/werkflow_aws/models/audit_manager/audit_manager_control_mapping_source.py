from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_source_keyword import AuditManagerSourceKeyword


class AuditManagerControlMappingSource(BaseModel):
    sourceId: StrictStr | None = None
    sourceName: StrictStr | None = None
    sourceDescription: StrictStr | None = None
    sourceSetUpOption: StrictStr | None = None
    sourceType: StrictStr | None = None
    sourceKeyword: AuditManagerSourceKeyword | None = None
    sourceFrequency: StrictStr | None = None
    troubleshootingText: StrictStr | None = None
