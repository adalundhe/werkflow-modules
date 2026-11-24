from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BulkAgentSessionInvocation(BaseModel):
    agentId: StrictStr | None = None
    issueId: StrictStr | None = None
    requestId: StrictStr | None = None
    userPrompt: StrictStr | None = None
