from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .preview_condition_group_configuration import PreviewConditionGroupConfiguration
from .preview_rule_configuration import PreviewRuleConfiguration
from .preview_trigger import PreviewTrigger
from .transition_link import TransitionLink


class TransitionPreview(BaseModel):
    actions: list[PreviewRuleConfiguration] | None = None
    conditions: PreviewConditionGroupConfiguration | None = None
    customIssueEventId: StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    links: list[TransitionLink] | None = None
    name: StrictStr | None = None
    toStatusReference: StrictStr | None = None
    transitionScreen: PreviewRuleConfiguration | None = None
    triggers: list[PreviewTrigger] | None = None
    type: StrictStr | None = None
    validators: list[PreviewRuleConfiguration] | None = None
