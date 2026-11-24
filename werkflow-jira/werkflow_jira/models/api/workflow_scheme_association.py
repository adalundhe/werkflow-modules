from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowSchemeAssociation(BaseModel):
    issueTypeIds: list[StrictStr] | None = None
    workflowId: StrictStr | None = None
