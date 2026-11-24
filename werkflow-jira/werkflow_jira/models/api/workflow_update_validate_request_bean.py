from __future__ import annotations
from pydantic import BaseModel
from .validation_options_for_update import ValidationOptionsForUpdate
from .workflow_update_request import WorkflowUpdateRequest


class WorkflowUpdateValidateRequestBean(BaseModel):
    payload: WorkflowUpdateRequest | None = None
    validationOptions: ValidationOptionsForUpdate | None = None
