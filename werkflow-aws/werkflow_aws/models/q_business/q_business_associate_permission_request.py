from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .q_business_permission_condition import QBusinessPermissionCondition


class QBusinessAssociatePermissionRequest(BaseModel):
    applicationId: StrictStr
    statementId: StrictStr
    actions: list[StrictStr]
    principal: StrictStr
    conditions: list[QBusinessPermissionCondition] | None = None
