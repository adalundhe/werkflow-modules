from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .condition_group_update import ConditionGroupUpdate
from .workflow_rule_configuration import WorkflowRuleConfiguration
from .workflow_transition_links import WorkflowTransitionLinks
from .workflow_trigger import WorkflowTrigger


class TransitionUpdateDTO(BaseModel):
    model_config = ConfigDict(extra="allow")

    actions: list[WorkflowRuleConfiguration] | None = None
    conditions: ConditionGroupUpdate | None = None
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
