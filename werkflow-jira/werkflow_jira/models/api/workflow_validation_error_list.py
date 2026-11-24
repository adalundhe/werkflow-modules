from __future__ import annotations
from pydantic import BaseModel
from .workflow_validation_error import WorkflowValidationError


class WorkflowValidationErrorList(BaseModel):
    errors: list[WorkflowValidationError] | None = None
