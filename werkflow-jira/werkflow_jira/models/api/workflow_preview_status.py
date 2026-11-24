from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .approval_configuration_preview import ApprovalConfigurationPreview
from .workflow_preview_layout import WorkflowPreviewLayout


class WorkflowPreviewStatus(BaseModel):
    approvalConfiguration: ApprovalConfigurationPreview | None = None
    deprecated: StrictBool | None = None
    layout: WorkflowPreviewLayout | None = None
    statusReference: StrictStr | None = None
