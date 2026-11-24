from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BackupPlanTemplatesListMember(BaseModel):
    BackupPlanTemplateId: StrictStr | None = None
    BackupPlanTemplateName: StrictStr | None = None
