from __future__ import annotations
from typing import Any
from pydantic import BaseModel, ConfigDict, Field as PydanticField, StrictStr
from .transition_screen_details import TransitionScreenDetails
from .workflow_rules import WorkflowRules


class Transition(BaseModel):
    model_config = ConfigDict(populate_by_name=True)

    description: StrictStr | None = None
    from_: list[StrictStr] | None = PydanticField(default=None, alias='from')
    id: StrictStr | None = None
    name: StrictStr | None = None
    properties: dict[StrictStr, Any] | None = None
    rules: WorkflowRules | None = None
    screen: TransitionScreenDetails | None = None
    to: StrictStr | None = None
    type: StrictStr | None = None
