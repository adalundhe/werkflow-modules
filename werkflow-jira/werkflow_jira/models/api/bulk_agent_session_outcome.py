from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .bulk_agent_session_item_error import BulkAgentSessionItemError


class BulkAgentSessionOutcome(BaseModel):
    agentId: StrictStr | None = None
    conversationId: StrictStr | None = None
    error: BulkAgentSessionItemError | None = None
    issueId: StrictStr | None = None
    requestId: StrictStr | None = None
    result: StrictStr | None = None
