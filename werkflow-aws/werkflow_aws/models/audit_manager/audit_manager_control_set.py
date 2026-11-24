from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .audit_manager_control import AuditManagerControl


class AuditManagerControlSet(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    controls: list[AuditManagerControl] | None = None
