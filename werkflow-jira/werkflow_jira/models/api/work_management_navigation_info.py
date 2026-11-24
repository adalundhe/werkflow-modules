from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkManagementNavigationInfo(BaseModel):
    boardName: StrictStr | None = None
