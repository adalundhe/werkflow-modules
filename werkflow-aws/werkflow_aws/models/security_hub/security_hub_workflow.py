from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubWorkflow(BaseModel):
    Status: StrictStr | None = None
