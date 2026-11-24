from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class ConnectContactSearchSummaryAiAgentInfo(BaseModel):
    AiAgentVersionId: StrictStr | None = None
    AiAgentEscalated: StrictBool | None = None
    AiUseCase: StrictStr | None = None
