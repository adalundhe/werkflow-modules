from __future__ import annotations
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictInt, StrictStr
from .condition_group_payload import ConditionGroupPayload
from .from_layout_payload import FromLayoutPayload
from .rule_payload import RulePayload
from .to_layout_payload import ToLayoutPayload


class TransitionPayload(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    actions: list[RulePayload] | None = None
    conditions: ConditionGroupPayload | None = None
    customIssueEventId: StrictStr | None = None
    description: StrictStr | None = None
    from_: list[FromLayoutPayload] | None = PydanticField(default=None, alias='from')
    id: StrictInt | None = None
    name: StrictStr | None = None
    properties: dict[StrictStr, StrictStr] | None = None
    to: ToLayoutPayload | None = None
    transitionScreen: RulePayload | None = None
    triggers: list[RulePayload] | None = None
    type: StrictStr | None = None
    validators: list[RulePayload] | None = None
