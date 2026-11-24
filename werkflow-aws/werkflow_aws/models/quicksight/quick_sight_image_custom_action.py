from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_image_custom_action_operation import QuickSightImageCustomActionOperation


class QuickSightImageCustomAction(BaseModel):
    CustomActionId: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Trigger: StrictStr | None = None
    ActionOperations: list[QuickSightImageCustomActionOperation] | None = None
