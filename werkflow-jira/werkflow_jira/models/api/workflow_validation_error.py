from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_element_reference import WorkflowElementReference


class WorkflowValidationError(BaseModel):
    additionalDetails: StrictStr | None = None
    code: StrictStr | None = None
    elementReference: WorkflowElementReference | None = None
    level: StrictStr | None = None
    message: StrictStr | None = None
    type: StrictStr | None = None
