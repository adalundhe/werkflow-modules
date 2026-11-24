from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .quick_sight_layer_custom_action_operation import QuickSightLayerCustomActionOperation


class QuickSightLayerCustomAction(BaseModel):
    CustomActionId: StrictStr | None = None
    Name: StrictStr | None = None
    Status: StrictStr | None = None
    Trigger: StrictStr | None = None
    ActionOperations: list[QuickSightLayerCustomActionOperation] | None = None
