from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubWorkflowUpdate(BaseModel):
    Status: StrictStr | None = None
