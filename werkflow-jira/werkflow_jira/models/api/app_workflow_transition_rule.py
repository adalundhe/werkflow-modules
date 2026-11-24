from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .rule_configuration import RuleConfiguration
from .workflow_transition import WorkflowTransition


class AppWorkflowTransitionRule(BaseModel):
    configuration: RuleConfiguration | None = None
    id: StrictStr | None = None
    key: StrictStr | None = None
    transition: WorkflowTransition | None = None
