from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LakeFormationAuditContext(BaseModel):
    AdditionalAuditContext: StrictStr | None = None
