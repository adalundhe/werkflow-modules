from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .available_workflow_trigger_types import AvailableWorkflowTriggerTypes


class AvailableWorkflowTriggers(BaseModel):
    availableTypes: list[AvailableWorkflowTriggerTypes] | None = None
    ruleKey: StrictStr | None = None
