from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_project_id_scope import WorkflowProjectIdScope


class WorkflowPreviewScope(BaseModel):
    project: WorkflowProjectIdScope | None = None
    type: StrictStr | None = None
