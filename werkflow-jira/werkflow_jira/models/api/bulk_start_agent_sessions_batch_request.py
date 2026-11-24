from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bulk_agent_session_invocation import BulkAgentSessionInvocation


class BulkStartAgentSessionsBatchRequest(BaseModel):
    clientMutationId: StrictStr | None = None
    invocations: list[BulkAgentSessionInvocation] | None = None
