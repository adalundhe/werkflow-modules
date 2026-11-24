from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class WorkflowHistoryItemDTO(BaseModel):
    isIntermediate: StrictBool | None = None
    workflowId: StrictStr | None = None
    workflowVersion: StrictInt | None = None
    writtenAt: StrictStr | None = None
