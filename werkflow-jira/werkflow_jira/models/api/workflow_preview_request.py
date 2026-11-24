from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowPreviewRequest(BaseModel):
    issueTypeIds: list[StrictStr] | None = None
    projectId: StrictStr | None = None
    workflowIds: list[StrictStr] | None = None
    workflowNames: list[StrictStr] | None = None
