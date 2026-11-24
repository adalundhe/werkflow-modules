from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_visual_custom_action_operation import QuickSightVisualCustomActionOperation


class QuickSightVisualCustomAction(BaseModel):
    CustomActionId: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Trigger: StrictStr | None = None
    ActionOperations: list[QuickSightVisualCustomActionOperation] | None = None
