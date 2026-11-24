from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .available_workflow_connect_rule import AvailableWorkflowConnectRule
from .available_workflow_forge_rule import AvailableWorkflowForgeRule
from .available_workflow_system_rule import AvailableWorkflowSystemRule
from .available_workflow_triggers import AvailableWorkflowTriggers


class WorkflowCapabilities(BaseModel):
    connectRules: list[AvailableWorkflowConnectRule] | None = None
    editorScope: StrictStr | None = None
    forgeRules: list[AvailableWorkflowForgeRule] | None = None
    projectTypes: list[StrictStr] | None = None
    systemRules: list[AvailableWorkflowSystemRule] | None = None
    triggerRules: list[AvailableWorkflowTriggers] | None = None
