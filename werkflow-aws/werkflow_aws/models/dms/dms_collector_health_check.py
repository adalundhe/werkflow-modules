from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class DMSCollectorHealthCheck(BaseModel):
    CollectorStatus: StrictStr | None = None
    LocalCollectorS3Access: StrictBool | None = None
    WebCollectorS3Access: StrictBool | None = None
    WebCollectorGrantedRoleBasedAccess: StrictBool | None = None
