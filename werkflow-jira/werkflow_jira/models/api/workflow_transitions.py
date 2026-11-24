from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .condition_group_configuration import ConditionGroupConfiguration
from .workflow_rule_configuration import WorkflowRuleConfiguration
from .workflow_transition_links import WorkflowTransitionLinks
from .workflow_trigger import WorkflowTrigger


class WorkflowTransitions(BaseModel):
    actions: list[WorkflowRuleConfiguration] | None = None
    conditions: ConditionGroupConfiguration | None = None
    customIssueEventId: StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    links: list[WorkflowTransitionLinks] | None = None
    name: StrictStr | None = None
    properties: dict[StrictStr, StrictStr] | None = None
    toStatusReference: StrictStr | None = None
    transitionScreen: WorkflowRuleConfiguration | None = None
    triggers: list[WorkflowTrigger] | None = None
    type: StrictStr | None = None
    validators: list[WorkflowRuleConfiguration] | None = None
