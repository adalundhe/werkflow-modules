from __future__ import annotations
from pydantic import BaseModel
from .app_flow_scheduled_trigger_properties import AppFlowScheduledTriggerProperties


class AppFlowTriggerProperties(BaseModel):
    Scheduled: AppFlowScheduledTriggerProperties | None = None
