from __future__ import annotations
from pydantic import BaseModel, StrictInt


class SWFWorkflowExecutionOpenCounts(BaseModel):
    openActivityTasks: StrictInt | None = None
    openDecisionTasks: StrictInt | None = None
    openTimers: StrictInt | None = None
    openChildWorkflowExecutions: StrictInt | None = None
    openLambdaFunctions: StrictInt | None = None
