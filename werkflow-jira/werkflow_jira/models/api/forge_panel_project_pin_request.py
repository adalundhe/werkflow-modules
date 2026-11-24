from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_pin_action import ProjectPinAction


class ForgePanelProjectPinRequest(BaseModel):
    moduleId: StrictStr | None = None
    projectList: list[ProjectPinAction] | None = None
