from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ECSDeploymentLifecycleHookDetail(BaseModel):
    hookId: StrictStr | None = None
    targetType: StrictStr | None = None
    targetArn: StrictStr | None = None
    status: StrictStr | None = None
    expiresAt: datetime.datetime | StrictStr | None = None
    timeoutAction: StrictStr | None = None
