from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ForgePanelProjectPinStatusRequest(BaseModel):
    moduleId: StrictStr | None = None
    projectList: list[StrictStr] | None = None
