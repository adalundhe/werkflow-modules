from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_action import GlueAction
from .glue_event_batching_condition import GlueEventBatchingCondition
from .glue_predicate import GluePredicate


class GlueTrigger(BaseModel):
    Name: StrictStr | None = None
    WorkflowName: StrictStr | None = None
    Id: StrictStr | None = None
    Type: StrictStr | None = None
    State: StrictStr | None = None
    Description: StrictStr | None = None
    Schedule: StrictStr | None = None
    Actions: list[GlueAction] | None = None
    Predicate: GluePredicate | None = None
    EventBatchingCondition: GlueEventBatchingCondition | None = None
