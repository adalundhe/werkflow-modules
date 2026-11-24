from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkflowSchemeProjectAssociation(BaseModel):
    projectId: StrictStr | None = None
    workflowSchemeId: StrictStr | None = None
