from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_association_status_mapping import WorkflowAssociationStatusMapping


class MappingsByWorkflow(BaseModel):
    newWorkflowId: StrictStr | None = None
    oldWorkflowId: StrictStr | None = None
    statusMappings: list[WorkflowAssociationStatusMapping] | None = None
