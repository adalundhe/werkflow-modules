from __future__ import annotations
from pydantic import BaseModel
from .project_result import ProjectResult


class BulkPolicyOperationResponse(BaseModel):
    failed: list[ProjectResult] | None = None
    successful: list[ProjectResult] | None = None
