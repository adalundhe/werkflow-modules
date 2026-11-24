from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BulkStartUniformAgentSessionsRequest(BaseModel):
    agentId: StrictStr | None = None
    clientMutationId: StrictStr | None = None
    issueIds: list[StrictStr] | None = None
    userPrompt: StrictStr | None = None
