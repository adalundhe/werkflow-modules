from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .bulk_agent_session_outcome import BulkAgentSessionOutcome


class BulkAgentSessionsResponse(BaseModel):
    alreadyStartedCount: StrictInt | None = None
    failedCount: StrictInt | None = None
    rateLimitedCount: StrictInt | None = None
    results: list[BulkAgentSessionOutcome] | None = None
    startedCount: StrictInt | None = None
    success: StrictBool | None = None
