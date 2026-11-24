from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessDisassociatePermissionRequest(BaseModel):
    applicationId: StrictStr
    statementId: StrictStr
