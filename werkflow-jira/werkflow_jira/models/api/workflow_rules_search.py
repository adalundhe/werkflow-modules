from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowRulesSearch(BaseModel):
    expand: StrictStr | None = None
    ruleIds: list[StrictStr] | None = None
    workflowEntityId: StrictStr | None = None
