from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .glue_action import GlueAction
from .glue_event_batching_condition import GlueEventBatchingCondition
from .glue_predicate import GluePredicate


class GlueCreateTriggerRequest(BaseModel):
    Name: StrictStr
    Type: Literal['SCHEDULED', 'CONDITIONAL', 'ON_DEMAND', 'EVENT']
    Actions: list[GlueAction]
    WorkflowName: StrictStr | None = None
    Schedule: StrictStr | None = None
    Predicate: GluePredicate | None = None
    Description: StrictStr | None = None
    StartOnCreation: StrictBool | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    EventBatchingCondition: GlueEventBatchingCondition | None = None
