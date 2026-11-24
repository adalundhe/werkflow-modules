from __future__ import annotations
from typing import TYPE_CHECKING
from pydantic import BaseModel, StrictStr

if TYPE_CHECKING:
    from .workflow_condition import WorkflowCondition


class WorkflowCompoundCondition(BaseModel):
    conditions: list[WorkflowCondition] | None = None
    nodeType: StrictStr | None = None
    operator: StrictStr | None = None
