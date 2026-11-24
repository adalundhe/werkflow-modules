from __future__ import annotations
from pydantic import BaseModel
from .validation_options_for_create import ValidationOptionsForCreate
from .workflow_create_request import WorkflowCreateRequest


class WorkflowCreateValidateRequest(BaseModel):
    payload: WorkflowCreateRequest | None = None
    validationOptions: ValidationOptionsForCreate | None = None
