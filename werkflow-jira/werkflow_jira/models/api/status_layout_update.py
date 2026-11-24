from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .approval_configuration import ApprovalConfiguration
from .workflow_layout import WorkflowLayout


class StatusLayoutUpdate(BaseModel):
    model_config = ConfigDict(extra="allow")

    approvalConfiguration: ApprovalConfiguration | None = None
    layout: WorkflowLayout | None = None
    properties: dict[StrictStr, StrictStr] | None = None
    statusReference: StrictStr | None = None
