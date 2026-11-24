from __future__ import annotations
from pydantic import BaseModel
from .event_bridge_run_command_target import EventBridgeRunCommandTarget


class EventBridgeRunCommandParameters(BaseModel):
    RunCommandTargets: list[EventBridgeRunCommandTarget] | None = None
