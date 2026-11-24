from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .approval_configuration import ApprovalConfiguration
from .workflow_status_layout import WorkflowStatusLayout


class WorkflowReferenceStatus(BaseModel):
    approvalConfiguration: ApprovalConfiguration | None = None
    deprecated: StrictBool | None = None
    layout: WorkflowStatusLayout | None = None
    properties: dict[StrictStr, StrictStr] | None = None
    statusReference: StrictStr | None = None
