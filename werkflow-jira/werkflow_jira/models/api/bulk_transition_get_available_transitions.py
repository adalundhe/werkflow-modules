from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .issue_bulk_transition_for_workflow import IssueBulkTransitionForWorkflow


class BulkTransitionGetAvailableTransitions(BaseModel):
    availableTransitions: list[IssueBulkTransitionForWorkflow] | None = None
    endingBefore: StrictStr | None = None
    startingAfter: StrictStr | None = None
