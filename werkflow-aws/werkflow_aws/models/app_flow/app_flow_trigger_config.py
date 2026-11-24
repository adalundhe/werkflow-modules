from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .app_flow_trigger_properties import AppFlowTriggerProperties


class AppFlowTriggerConfig(BaseModel):
    triggerType: StrictStr | None = None
    triggerProperties: AppFlowTriggerProperties | None = None
