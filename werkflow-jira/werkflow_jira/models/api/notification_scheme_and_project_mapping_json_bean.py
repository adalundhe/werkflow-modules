from __future__ import annotations
from pydantic import BaseModel, StrictStr


class NotificationSchemeAndProjectMappingJsonBean(BaseModel):
    notificationSchemeId: StrictStr | None = None
    projectId: StrictStr | None = None
