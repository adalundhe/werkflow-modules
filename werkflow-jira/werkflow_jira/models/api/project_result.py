from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .policy_application_violation import PolicyApplicationViolation


class ProjectResult(BaseModel):
    errors: list[PolicyApplicationViolation] | None = None
    message: StrictStr | None = None
    projectId: StrictInt | None = None
