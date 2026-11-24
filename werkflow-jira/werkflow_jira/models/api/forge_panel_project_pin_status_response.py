from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .forge_panel_project_pin_status import ForgePanelProjectPinStatus


class ForgePanelProjectPinStatusResponse(BaseModel):
    moduleId: StrictStr | None = None
    statuses: list[ForgePanelProjectPinStatus] | None = None
